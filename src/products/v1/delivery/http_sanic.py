from sanic import Blueprint
from sanic.response import json, html, redirect
from src.products.v1.repository.product_repo_orator import ProductRepositoryOrator
from src.products.v1.usecase.product_usecase import ProductCreateUseCase, ProductListUseCase, ProductDetailUseCase
from src.products.v1.usecase.request_object import ProductCreateRequestObject, ProductListRequestObject, \
    ProductDetailRequestObject
from src.shared.request.request_sanic import RequestSanicDict

bp_products = Blueprint('productsV1', url_prefix='/')


@bp_products.route('/', methods=['GET'])
async def index(request):
    request_dict = RequestSanicDict(request)
    data = request_dict.parse_all_to_dict()

    request_object = ProductListRequestObject.from_dict(data)
    repo = ProductRepositoryOrator(db=request.app.db)
    use_case = ProductListUseCase(repo=repo)
    response = use_case.execute(request_object=request_object)

    template = request.app.env.get_template('index.html')
    html_content = template.render(response=response.value, app=request.app)
    return html(html_content)


@bp_products.route('/add', methods=['GET', 'POST'])
async def add(request):
    flash = dict()
    request_dict = RequestSanicDict(request)
    if request.method == 'POST':
        data = request_dict.parse_all_to_dict()

        request_object = ProductCreateRequestObject.from_dict(data)
        repo = ProductRepositoryOrator(db=request.app.db)
        use_case = ProductCreateUseCase(repo=repo)
        response = use_case.execute(request_object=request_object)
        if response.type == 'SUCCESS':
            return redirect(request.app.url_for("productsV1.index"))

        flash = {
            'icon': 'danger',
            'title': 'Errors!',
            'message': response.message
        }

    template = request.app.env.get_template('add-product.html')
    html_content = template.render(app=request.app, flash=flash)
    return html(html_content)


@bp_products.route('/detail/<identifier:string>', methods=['GET'])
async def detail(request, identifier):
    request_dict = RequestSanicDict(request)

    data = request_dict.parse_all_to_dict()
    data["id"] = identifier
    request_object = ProductDetailRequestObject.from_dict(data)
    repo = ProductRepositoryOrator(db=request.app.db)
    use_case = ProductDetailUseCase(repo=repo)
    response = use_case.execute(request_object=request_object)

    template = request.app.env.get_template('detail-product.html')
    html_content = template.render(app=request.app, item=response.value)
    return html(html_content)
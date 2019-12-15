from unittest import mock

import pytest
import requests_mock

from src.app import connect_db
from src.products.v1.repository.product_repo_orator import ProductRepositoryOrator
from src.products.v1.usecase.product_usecase import ProductListUseCase, ProductDetailUseCase, ProductCreateUseCase
from src.products.v1.usecase.request_object import ProductListRequestObject, ProductDetailRequestObject, \
    ProductCreateRequestObject


@pytest.fixture(scope="module")
def db_con():
    db = connect_db()
    yield db
    db.disconnect()


def test_product_list(db_con):
    repo = ProductRepositoryOrator(db=db_con)

    use_case = ProductListUseCase(repo=repo)
    request_object = ProductListRequestObject.from_dict(data={})

    response_object = use_case.execute(request_object)

    assert response_object.type == 'SUCCESS'


def test_product_detail_not_found(db_con):
    repo = ProductRepositoryOrator(db=db_con)

    use_case = ProductDetailUseCase(repo=repo)
    request_object = ProductDetailRequestObject.from_dict(data={'id': 1999})

    response_object = use_case.execute(request_object)

    assert response_object.type != 'SUCCESS'


def test_product_create_wrong_url(db_con):
    repo = ProductRepositoryOrator(db=db_con)

    use_case = ProductCreateUseCase(repo=repo)
    request_object = ProductCreateRequestObject.from_dict(data={'url': "coba123"})

    response_object = use_case.execute(request_object)

    assert response_object.type != 'SUCCESS'


def test_product_create_empty_url(db_con):
    repo = ProductRepositoryOrator(db=db_con)

    use_case = ProductCreateUseCase(repo=repo)
    request_object = ProductCreateRequestObject.from_dict(data={'url': ""})

    response_object = use_case.execute(request_object)

    assert response_object.type != 'SUCCESS'


def test_product_create(db_con):
    url = "https://fabelio.com/ip/test.html"
    html = '<script type="application/ld+json" class="y-rich-snippet-script">{"@context":"http://schema.org","@type":"Product","image":"https://fabelio.com/static/version1575905947/frontend/Fabelio/aurela/id_ID//d/c/dc-1724-patch2-1_1.jpg","name":"KursiCessiUpholstered","brand":"Fabelio","description":"<p>KursiUrbanStyleyangNyaman</p><p>Merombaktampilanrumahakanlebihmudahdenganhadirnyafurnituryangindah.CessiUpholsteredChairsanggupmemenuhiitusemuadengandesainnyayangberkonsepurbanstyledilengkapidenganarmrest.Selainkarenanyaman,kursiinisangattepatdigunakanbagikalianyangberjiwamudadaninginmenjadikanhunianlebihberwarna.Dilengkapidenganmaterialsolidwoodyangkuatdandudukanbusaempuk,kursiinidapatkaliangunakanuntukmenemanimakanmalamatausaatkalianbekerja.</p>","url":"https://fabelio.com/ip/kursi-cessi-upholstered.html","sku":"KAYUA001","width":"0","height":"0","weight":"10","offers":{"@type":"offer","availability":"http://schema.org/InStock","price":"699000","priceCurrency":"IDR"}}</script>'
    with requests_mock.Mocker() as request_mocker:
        request_mocker.register_uri('GET', url, text=html)
        repo = ProductRepositoryOrator(db=db_con)
        use_case = ProductCreateUseCase(repo=repo)
        request_object = ProductCreateRequestObject.from_dict(data={'url': url})
        response_object = use_case.execute(request_object)
        last_id = response_object.value['id']

        assert response_object.type == 'SUCCESS'

        # Re create
        response_object = use_case.execute(request_object)
        assert response_object != 'SUCCESS'

        # Find detail
        use_case = ProductDetailUseCase(repo=repo)
        request_object = ProductDetailRequestObject.from_dict(data={'id': last_id, 'crawl': 'true'})
        response_object = use_case.execute(request_object)
        assert response_object.type == 'SUCCESS'

        # delete last add
        repo.delete(last_id)

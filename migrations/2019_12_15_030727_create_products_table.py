from orator.migrations import Migration


class CreateProductsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('products') as table:
            table.increments('id')
            table.string('sku').nullable()
            table.string('name').nullable()
            table.string('brand').nullable()
            table.long_text('image').nullable()
            table.long_text('description').nullable()
            table.string('width').nullable()
            table.string('height').nullable()
            table.string('weight').nullable()
            table.integer('price').nullable()
            table.string('price_currency').nullable()
            table.long_text('url')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('products')

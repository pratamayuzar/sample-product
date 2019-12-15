from orator.migrations import Migration


class CreateHistoryPriceTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('history_price') as table:
            table.increments('id')
            table.string('product_id')
            table.integer('price')
            table.string('price_currency')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('history_price')

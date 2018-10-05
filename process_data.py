import os, sys  # DEBUG
import csv
import logging
import dateutil.parser

from sqlalchemy import exc

from models.base import db
from models.Customer import CustomerModel
from models.Product import ProductModel
from models.Purchase import PurchaseModel

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))  # DEBUG


class process_data():
    def import_tsv(self, filepath):
        # logger.debug('Filepath: ' + filepath)  # DEBUG

        line_count = 0

        with open(filepath, newline='') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)

            reader = csv.DictReader(csvfile, dialect=dialect)

            for row in reader:
                # DEBUG
                # if line_count > 10:
                #     break

                line_count += 1

                date_parsed = dateutil.parser.parse(row['date']).strftime("%Y-%m-%d %H:%M:%S")

                # Customer
                customer = self.getRecord(CustomerModel, {'id': row['customer_id']})
                customer.id = row['customer_id']
                customer.first_name = row['first_name']
                customer.last_name = row['last_name']
                customer.address = row['address']
                customer.state = row['state']
                customer.postal_code = row['postal_code']

                db.session.add(customer)

                # Product
                product = self.getRecord(ProductModel, {'id': row['product_id']})
                product.id = row['product_id']
                product.name = row['product_name'].encode("utf-8")

                db.session.add(product)

                # Purchase
                purchase = self.getRecord(PurchaseModel, {
                    'customer_id': customer.id,
                    'product_id': row['product_id'],
                    'date': date_parsed})
                purchase.customer_id = row['customer_id']
                purchase.status = row['order_status']
                purchase.product_id = row['product_id']
                purchase.amount = row['purchase_amount'].replace('$', '')
                purchase.date = date_parsed

                db.session.add(purchase)

                db.session.commit()

        # DEBUG
        logger.info('Processed {} records'.format(line_count))

    def getRecord(self, model, filters):
        try:
            result = db.session.query(model).filter_by(**filters).one()
            # logger.info('Updating ' + model.__name__ + ' record.')
        except exc.SQLAlchemyError:
            result = model()
            # logger.info('New ' + model.__name__ + ' record found.')

        return result


# DEBUG - uncomment this to run the
# filepath = os.path.abspath('./atlantic_data.txt')
# process_data().import_tsv(filepath)

import os,sys
from google.cloud import bigquery

class BigqueryParser():

    def __init__(self, project, bq_dataset):
        '''
        project = 'bigquery-public-data
        bq_dataset = 'crypto_bitcoin'
        '''
        try:
            self.client = bigquery.Client()
            self.hn_dataset_ref = self.client.dataset(bq_dataset, project=project)
            self.hn_dset = self.client.get_dataset(self.hn_dataset_ref)
        except Exception as E:
            print(E)

    def get_tableList(self):
        #read list of tables
        [print(x.table_id) for x in self.client.list_tables(self.hn_dset)]

    def get_tableSchema(self, table_key):
        #read schema
        hn_full = self.client.get_table(self.hn_dset.table(table_key))
        print(hn_full.schema)

    def run_query(self, table_key, toJoin_array=None, location="US"):
        '''
        This function will be returned to you do requests for getting data from BigQuery
        '''
        hn_dset = self.client.get_dataset(self.hn_dataset_ref)
        hn_full = self.client.get_table(hn_dset.table(table_key))
        standard_query = hn_full.view_query
        query = (str(standard_query))

        self.query_job = None
        if toJoin_array is None:
            self.query_job = self.client.query(
                query,
                location=location)

        else:
            self.query_job = self.client.query(
                query + ' ' + str(toJoin_array),
                location=location)

    def read(self, file_name=None):
        #It will be saved to tmp directory.
        for row in self.query_job:
            if file_name is None:
                print(dict(row))
            else:
                file_name = os.path.join('/tmp/', file_name)
                with open(file_name, 'a') as f:
                    f.write(str(dict(row)) + str('\n'))
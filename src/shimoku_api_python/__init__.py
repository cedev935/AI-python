from __future__ import absolute_import
import logging
from shimoku_api_python.execution_logger import configure_logging, logging_before_and_after
import shimoku_api_python.async_execution_pool
from shimoku_api_python.async_execution_pool import async_auto_call_manager, ExecutionPoolContext
# import apis into sdk package
from shimoku_api_python.api.universe_metadata_api import UniverseMetadataApi
from shimoku_api_python.api.business_metadata_api import BusinessMetadataApi
from shimoku_api_python.api.dashboard_metadata_api import DashboardMetadataApi
from shimoku_api_python.api.app_metadata_api import AppMetadataApi
from shimoku_api_python.api.app_type_metadata_api import AppTypeMetadataApi
from shimoku_api_python.api.report_metadata_api import ReportMetadataApi
from shimoku_api_python.api.data_managing_api import DataManagingApi
from shimoku_api_python.api.file_metadata_api import FileMetadataApi
from shimoku_api_python.api.plot_api import PlotApi
from shimoku_api_python.api.ai_api import AiAPI
from shimoku_api_python.api.ping_api import PingApi
from shimoku_api_python.api.activity_metadata_api import ActivityMetadataApi

from shimoku_api_python.client import ApiClient

import shimoku_components_catalog.html_components
# from shimoku_api_python.configuration import Configuration
logger = logging.getLogger(__name__)


class Client(object):

    @logging_before_and_after(logging_level=logger.debug)
    def __init__(self, universe_id: str, environment: str = 'production',
                 access_token: str = '', config={}, business_id: str = '',
                 verbosity: str = None, async_execution: bool = False):

        self.configure_logging = configure_logging
        if verbosity:
            self.configure_logging(verbosity)

        if access_token and access_token != "":
            config = {'access_token': access_token}

        self._api_client = ApiClient(
            config=config,
            universe_id=universe_id,
            environment=environment,
        )

        self.epc = ExecutionPoolContext(api_client=self._api_client)

        if async_execution:
            self.activate_async_execution()
        else:
            self.activate_sequential_execution()

        self.ping = PingApi(self._api_client)
        self.universe = UniverseMetadataApi(self._api_client, execution_pool_context=self.epc)
        self.business = BusinessMetadataApi(self._api_client, execution_pool_context=self.epc)
        self.dashboard = DashboardMetadataApi(self._api_client, self.business, business_id=business_id,
                                              execution_pool_context=self.epc)
        self.app_type = AppTypeMetadataApi(self._api_client, execution_pool_context=self.epc)
        self.app = AppMetadataApi(self._api_client,
                                  business_id=business_id,
                                  execution_pool_context=self.epc,
                                  dashboard_metadata_api=self.dashboard)
        self.report = ReportMetadataApi(self._api_client)
        self.data = DataManagingApi(self._api_client)
        self.io = FileMetadataApi(self._api_client, business_id=business_id, execution_pool_context=self.epc)
        self.plt = PlotApi(self._api_client, business_id=business_id, app_metadata_api=self.app,
                           execution_pool_context=self.epc)

        self.epc.plot_api = self.plt

        self.ai = AiAPI(self.plt)
        self.html_components = shimoku_components_catalog.html_components
        self.activity = ActivityMetadataApi(self._api_client,
                                            app_metadata_api=self.app,
                                            business_metadata_api=self.business,
                                            plot_api=self.plt,
                                            business_id=business_id,
                                            execution_pool_context=self.epc)

    @logging_before_and_after(logging_level=logger.info)
    def set_config(self, config={}):
        self._api_client.set_config(config)

    @async_auto_call_manager(execute=True)
    async def run(self):
        pass

    def activate_async_execution(self):
        self.epc.sequential = False

    def activate_sequential_execution(self):
        self.epc.sequential = True

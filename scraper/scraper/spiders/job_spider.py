# import scrapy
# import json
# import logging
# from urllib.parse import urlencode


# class JobSpider(scrapy.Spider):
#     name = "job_spider"
#     allowed_domains = ["job-search-api.svc.dhigroupinc.com"]

#     def start_requests(self):
#         url = "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search"
#         headers = {
#             'x-api-key': '1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
#         }
#         params = {
#             'q': 'Software',
#             'countryCode2': 'US',
#             'radius': '30',
#             'radiusUnit': 'mi',
#             'page': '1',
#             'pageSize': '20',
#             'fields': 'title|companyName|location|salary|detailsPageUrl|postedDate|employmentType|skills|updatedDate',
#         }

#         yield scrapy.Request(
#             url=f"{url}?{self.build_query_string(params)}",
#             headers=headers,
#             callback=self.parse,
#             meta={'headers': headers, 'params': params}
#         )

#     def parse(self, response):
#         if response.status != 200:
#             self.logger.error(f"Request failed with status: {response.status}")
#             return

#         try:
#             data = json.loads(response.text)
#         except json.JSONDecodeError:
#             self.logger.error("Failed to decode JSON response")
#             return

#         # Extract jobs if available
#         jobs = data.get('data', [])
#         if not jobs:
#             self.logger.info("No more jobs found. Stopping pagination.")
#             return

#         for job in jobs:
#             yield {
#                 'title': job.get('title'),
#                 'postedDate': job.get('postedDate'),
#                 'updatedDate': job.get('updatedDate'),
#                 'detailsPageUrl': job.get('detailsPageUrl'),
#                 'salary': job.get('salary'),
#                 'employementType': job.get('employmentType'),
#                 'skills': job.get('skills'),
#                 'companyName': job.get('companyName'),
#             }

#         # Handle pagination if more pages are available
#         meta = response.meta
#         current_page = int(meta['params']['page'])
#         meta['params']['page'] = str(current_page + 1)
#         next_url = f"{response.url.split('?')[0]}?{self.build_query_string(meta['params'])}"
#         yield scrapy.Request(
#             url=next_url,
#             headers=meta['headers'],
#             callback=self.parse,
#             meta=meta
#         )

#     @staticmethod
#     def build_query_string(params):
#         """Helper function to build a query string from a dictionary of parameters."""
#         return urlencode(params)


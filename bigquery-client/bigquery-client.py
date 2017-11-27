# Imports the Google Cloud client library
from google.cloud import bigquery
import time

# Instantiates a client
client = bigquery.Client(project='httparchive-stats')

# Construct the query object
query = client.run_sync_query("""\
SELECT
  NTH(50, quantiles(TTFB))   TTFB_med,
  NTH(50, quantiles(renderStart))   START_RENDER_med,
  NTH(50, quantiles(onLoad))   ONLOAD_med,
  NTH(50, quantiles(visualComplete))   VISUAL_COMPLETE_med,
  NTH(50, quantiles(SpeedIndex))   SPEED_INDEX_med,
  NTH(50, quantiles(reqTotal))   TOTAL_reqs_med,
  NTH(50, quantiles(bytesTotal))   TOTAL_med,
  NTH(50, quantiles(reqImg))     IMG_reqs_med,
  NTH(50, quantiles(bytesImg))     IMG_med,
  NTH(50, quantiles(reqJS))      JS_reqs_med,
  NTH(50, quantiles(bytesJS))      JS_med,
  NTH(50, quantiles(reqCSS))     CSS_reqs_med,
  NTH(50, quantiles(bytesCSS))     CSS_med,
  NTH(50, quantiles(reqHtml))    HTML_reqs_med,
  NTH(50, quantiles(bytesHtml))    HTML_med,
  NTH(50, quantiles(reqFont))    FONT_reqs_med,
  NTH(50, quantiles(bytesFont))    FONT_med,
  NTH(50, quantiles(numDomains))    DOMAINS_med,
  NTH(50, quantiles(numDomElements))    DOM_ELEMS_med,
FROM [httparchive:runs.2017_11_15_pages_mobile]
WHERE rank <= 1000
""")

# Execute the query
query.run()

rows = query.fetch_data()

for row in rows:
    # Convert tuple to list and print
    print (row)

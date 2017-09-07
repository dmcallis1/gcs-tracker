# gcs-tracker

The purpose of this project is to provide an automated mechanism for seeding a [recommendation tracker document](https://ac.akamai.com/docs/DOC-32597#jive_content_id_Recommendation_Tracker), used by [GCS Consulting](https://ac.akamai.com/community/teams/gss/global-services/gcs/consulting).

The recommendation tracker contain a variety of page speed and weight metrics collected for customers. These customer specific metrics are compared against synthetic benchmarks obtained from [HTTPArchive.org](www.httparchive.org) to provide context to the customer on how their page performance compares to global medians.

Since this is a common deliverable for all GCS consulting engagements, considerable time could be saved by automating the generation of these metrics.

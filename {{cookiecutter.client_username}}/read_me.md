Hi, {{cookiecutter.client_username}}! 

Thank you for your trust in using my services. I hope this helps according to your needs! Here's the summary about your orders:

* date order : {{cookiecutter.order_date}}
* package chosen : {{cookiecutter.packaged_chosen}}
* package summary : {% if cookiecutter.packaged_chosen == 'Basic' %}
    * Scrape features: 
    * File output: .csv, .xslx, .sql
    * 1 day delivery
    * Unlimited revisions
    * Price: $5
{% elif cookiecutter.packaged_chosen == 'Standard' %}
    * Scrape features: 
    * Include data preprocessing to clean the data collection using Tableau Prep
    * File output: .csv, .xslx, .sql
    * 2 days delivery
    * Unlimited revisions
    * Price: $15
{% elif cookiecutter.packaged_chosen == 'Premium' %}
    * Scrape features: 
    * Include data preprocessing to clean the data collection using Tableau Prep
    * File output: .csv, .xslx, .sql
    * 3 days delivery
    * Unlimited revisions
    * Price: $30
{% endif %}
* request description : 
{{cookiecutter.request}}

--------------------------------
Author: Harits Muhammad
LinkedIn: https://www.linkedin.com/in/haritsmuhammad/
Fiverr: fiverr.com/haritsmhmd
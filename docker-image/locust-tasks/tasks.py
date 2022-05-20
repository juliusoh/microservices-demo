#!/usr/bin/env python

# Copyright 2022 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid

from datetime import datetime
from locust import FastHttpUser, TaskSet, task


# [START locust_test_task]

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())



    @task(999)
    def add_cart(self):
        products = ["OLJCESPC7Z", "66VCHSJNUP", "1YMWWN1N4O", "L9ECAV7KIM", "2ZYFJ3GM2N", "0PUK6V6EV0", "LS4PSXUNUM", "9SIQT8TOJO", "6E92ZMYYFZ"]
        for item in products:
            self.client.post(
            '/cart', {"product_id": item, "quantity": 1})


    @task(999)
    def post_checkout(self):
        self.client.post(
            "/cart/checkout", {"email": "someone@example.com", "street_address": "1600+Amphitheatre+Parkway", "zip_code": 94043, "city": "Mountain View", "state": "CA", "country": "United States", "credit_card_number": "4432-8015-6152-0454", "credit_card_expiration_month": 1, "credit_card_expiration_year": 2023, "credit_card_cvv": 672})


class MetricsLocust(FastHttpUser):
    tasks = {MetricsTaskSet}

# [END locust_test_task]

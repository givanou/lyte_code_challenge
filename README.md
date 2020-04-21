# Lyte Code challenge api
* **Base URL of deployed app**

https://lyte-code-challenge.herokuapp.com/


**Event List Endpoint**
----
 
* **URL**

  /events

* **Methods:**
  
  

       `GET` 
  
*  **URL Params**

   **Optional:**
 
   `name=[string]`
   
   `promoter_name=[string]`
   
   `price=[decimal]`
   
   `start_date=[%Y-%m-%d]`


* **Sample Call:**

    curl "https://lyte-code-challenge.herokuapp.com/events?name=hamil&start_date=2020-12-07"


* **Success Response:**

    Code: 200 <br />
    **Content:** `[
    {
        "id": "1Ad7ZpeGkDcB3Uf",
        "name": "Hamilton (Touring)",
        "description": null,
        "url": "https://www.ticketmaster.ca/hamilton-touring-ottawa-ontario-12-06-2020/event/3100582EEDE92D94",
        "start_date": "2020-12-07T00:30:00Z",
        "end_date": null,
        "promoter_name": "NATIONAL ARTS CENTRE (CANADA)",
        "prices": [
            {
                "currency": "CAD",
                "price_type": "standard",
                "max_price": "344.00",
                "min_price": "80.00"
            }
        ]
    }
]`
* **Notes:**

  Sadly, current system of price filtering does not support currency conversion.
  When you want to filter events by price it just checks if price get in between of min and max price values.
   
**Event Update Endpoint**
----
 
* **URL**

  /update/<str:id>

* **Methods:**
  
       `PUT` | `PATCH` 

* **Sample Call:**

    curl -X PUT -H "Content-Type: application/json" -d "{'id':'1Ad7ZpeGkDcB3Uf','name':'AmazingNewName'}" https://lyte-code-challenge.herokuapp.com/update/1Ad7ZpeGkDcB3Uf

* **Success Response:**

    HTTP 200 OK
    
    Content-Type: application/json
    
    Vary: Accept

    **Content:** `{
    "id": "1Ad7ZpeGkDcB3Uf",
    "name": "AmazingNewName",
    "description": null,
    "url": "https://www.ticketmaster.ca/hamilton-touring-ottawa-ontario-12-06-2020/event/3100582EEDE92D94",
    "start_date": "2020-12-07T00:30:00Z",
    "end_date": null,
    "promoter_name": "NATIONAL ARTS CENTRE (CANADA)",
    "prices": [
        {
            "currency": "CAD",
            "price_type": "standard",
            "max_price": "344.00",
            "min_price": "80.00"
        }
    ]
}
]`
* **Notes:**

  You can use DRF Forms on page itself to test the api
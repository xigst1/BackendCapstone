

### path for API:

- get/post menu
http://127.0.0.1:8000/restaurant/menu/

- get/put/delete single menu item
http://127.0.0.1:8000/restaurant/menu/pk


- get/post table booking
http://127.0.0.1:8000/restaurant/booking/tables/

### unit test

1. please comment out the 'permission_classes = [IsAuthenticated]' lines in both MenuItemView and BookingViewSet classes prior to unit test in terminal
2. Somehow I am not able to run the unit test without specifying the path of tests folder. Please use following command in the terminal. 


python manage.py test littlelemon/tests

It will be great to learn how to execute the test with 'python manage.py test' like what the instruction indicates.

### Test menu and booking APIs in browser
- please comment out the 'permission_classes = [IsAuthenticated]' lines in both MenuItemView and BookingViewSet classes prior to test APIs in browser




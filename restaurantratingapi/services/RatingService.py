from rest_framework.exceptions import APIException
from ..models import Rating
from ..models import AddedDishRating
from ..models import Dish
from ..models import Restaurant
from ..models import User
from ..models import Token
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
from .ValidationService import ValidationService
from django.db import IntegrityError

class RatingService:

    def __init__(self):
        self.data = [];

    def add_rating(self, data):
        # retrieve request data
        try:
            # print(data)
            # print('vdssssssssdata')
            username = data['user']
            token_number = data['token_number'] #token number 
            rest_id = data['restaurant_id'] #restaurant id #required
            # rating = data['rating'];
            dish_id = data['dish_id'] #dish id
            dish_rating = data['dish_rating'] #dish rating #required
            price_rating = data['price_rating'] #price rating #required
            service_rating = data['service_rating'] #service rating #required
            review = data['review'] #review #required
            # rest_longitude = data['longitude'] #restaurant GEO location-longitude #required
            # rest_latitude = data['latitude'] #restaurant GEO location-latitude #required
            # selected_role = data['role'] #user's requested role for the restaurant
        except KeyError as e:
            raise APIException(f"Key {e} not exists in the request")

        # validate request data for null or empty values
        if(not ValidationService.isset(value=rest_id)):
            raise APIException("Restaurant id is empty")

        if(not ValidationService.isset(value=price_rating)):
            raise APIException("Price rating is empty")

        if(not ValidationService.isset(value=service_rating)):
            raise APIException("Service rating is empty")    

        if(not ValidationService.isset(value=review)):
            raise APIException("Review is empty") 

        # validate request data values for db existance
        if(not isinstance(username, str)):
            raise APIException("Username should be string")

        # dish rating integer validation
        # dish rating range validation

        # price rating integer validation
        # price rating range validation

        # service rating integer valiation
        # service rating range validation

        # check user exists
        # check whether the username exists

        # user = User.objects.get(username=username)
        # if(not user):
        #     raise APIException(f"Username name '{username}' not exists")

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist as e:
            raise APIException(f"Username name '{username}' not exists")
            
        # check user logged in

        # validate restaurant id
        # check whether the restaurant id exists

        # restaurant = Restaurant.objects.get(restaurant_id=rest_id)

        # if(not restaurant):
        #     raise APIException(f"Restaurant id '{rest_id}' not exists")
        
        try:
            restaurant = Restaurant.objects.get(restaurant_id=rest_id)
        except ObjectDoesNotExist as e:
            raise APIException(f"Restaurant id '{rest_id}' not exists")

        # validate dish id(if exists)
        # dish = Dish.objects.get(dish_id=dish_id)

        # if(not dish):
        #     raise APIException(f"Dish id '{dish_id}' not exists")

        try:
            dish = Dish.objects.get(dish_id=dish_id)
        except ObjectDoesNotExist as e:
            raise APIException(f"Dish id '{dish_id}' not exists")

        # token = Token.objects.get(token_number=token_number, restaurant=restaurant)

        # if(not token):
        #     raise APIException(f"Token number '{token_number}' not exists")

        try:
            token = Token.objects.get(token_number=token_number, restaurant=restaurant)
        except ObjectDoesNotExist as e:
            token = None
            # raise APIException(f"Token number '{token_number}' not exists")

        # validate rating categories

        if(token == None):
            verified = 0
        else:
            # validate token number
            verified = 1

        rating = Rating(
          dish_rating = dish_rating,
          price_rating = price_rating,
          service_rating = service_rating,
          verified = verified,
          created_on = "2020-06-26")

        try: 
            rating.save()
        except IntegrityError as e:
            raise APIException(e)  

        if(dish_id != None):
            added_dish_rating = AddedDishRating(
            rating = rating,
            restaurant = restaurant,
            dish = dish,
            user = user,
            token_number = token)

        try: 
            pass
            # rating.save()
        except IntegrityError as e:
            raise APIException(e)   

        # add contribution points to the user

        # this should be change by using response model
        resp={
            "success": True,
            "code": 200,
            "message": "success AddRating",
            "data": {
                # "restaurant_id": rating.restaurant_id,
                # "rated_by": rest.created_by.id,
                "verified": rating.verified,
                "dish_rating": rating.dish_rating,
                "price_rating": rating.price_rating,
                "service_rating": rating.service_rating
            }
        }

        return resp  

    def delete_rating(self, data):
        pass;
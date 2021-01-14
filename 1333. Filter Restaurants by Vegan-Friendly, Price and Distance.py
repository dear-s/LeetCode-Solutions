
        
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
        
        # [id, rating, veganFriendly, price, distance]
        
        answer = []
        id_rating = [] # after filtering
        
        for rest in restaurants:
            one = rest[0] # id
            two = rest[1] # rating
            three = rest[2] # veganFriendly
            four = rest[3] # price
            five = rest[4] # distance
            
            if (veganFriendly == 1 and three == 1) or (veganFriendly == 0):
                # add veganFriendly
                if four <= maxPrice and five <= maxDistance:
                    id_rating.append([one, two])
            
        # print("id_rating: ", id_rating)
        
        # update answer array
        
        # reverse sort -- id, then rating
        id_rating.sort(key = lambda x:x[0], reverse = True)
        id_rating.sort(key = lambda x:x[1], reverse = True)
        
        for x in id_rating:
            answer.append(x[0])
            
        return answer
        


		

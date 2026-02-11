from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

#get means http get , whiich is the standard web method for requesting data !
#so when y


#when a request comes in !
# fastapi recieves it at the app , inside the router , it looks for a route ! that matches the http method (get) and the
#path (/health)
# so @router.get("/health") stores this method-path-function  inside the apirouter object!
#@router.get("/health") resgisturrs http method(get) ,the path("/health")
#what is http ,, it is a set of rules thsat computers use to send and recieve requests from the internet
#http is like the road
#api , this is the list of endpoints your server exposes over http
# each endpoint is defined by a methood + path + behavior
#api exposes the endpoints to the client
#api does not expose requests
#it defines end points
#what paths exist and what they do !
#http defines (format)  how requests are sent and recieved
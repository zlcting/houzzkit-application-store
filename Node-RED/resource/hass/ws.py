import sys,os,json
from websocket import create_connection
url = "ws://localhost:8123/api/websocket"
def init_hass_ws(ws,token):
    msg = {
        "type":"auth",
        "access_token":token,
    }
    send_msg = json.dumps(msg)
    
    ws.send(send_msg)
    result =  ws.recv()
    # print(result)



def short_connection(url,send_msg,token):
    ws = create_connection(url)
    ws.recv()
    init_hass_ws(ws,token)
    #print("Sending 'Hello, World'...")
    ws.send(send_msg)
    # print("Sent")
    # print("Receiving...")
    result =  ws.recv()
    # print("Received '%s'" % result)
    ws.close()
    return result

def hass_restart(id,token):
    data = {
		"type":        "call_service",
		"domain":      "homeassistant",
		"service":     "restart",
		"service_data": {},
		"id":          id,
	}
    ws = create_connection(url)
    # print(ws.recv())
    init_hass_ws(ws,token)
    send_msg = json.dumps(data)
    # print("Sending"+send_msg)
    ws.send(send_msg)
    # print("Receiving...")
    result =  ws.recv()
    ws.close()
    return result


if __name__ == '__main__':
    short_connection("ws://echo.websocket.events/","asdasdasdsa")


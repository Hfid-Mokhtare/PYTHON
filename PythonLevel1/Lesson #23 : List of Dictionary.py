ContacteInfo={
    "facebook_acounte":str,
    "tweeter_acounte":str,
    "emaile":str,
    "phone":str
}

PersonalInfo={
    "FullName":str,
    "Age":int,
    "gender":chr

}

CartInfo={
    "ContacteInfo":ContacteInfo,
    "PersonalInfo":PersonalInfo
}

def ReadInfo(CartInfo):
    print("-"*50)
    for data_k, data_v in CartInfo.items():
        for info_k in data_v:
            data_v[info_k]=input(f"enter {info_k} : ")
    return CartInfo

def PrintInfo(CartInfo):
    print("-"*50)
    for data_k, data_v in CartInfo.items():
        for info_k, info_v in data_v.items():
            print(f"{info_k} : {info_v}")


def AddClient(CartInfo):
    clients=[]
    for i in range(2):
        client=ReadInfo(CartInfo)
        clients.append(client)
    return clients   

def PrintClients(clients):
    for i in range(2):
        PrintInfo(clients[i])
    

clients = AddClient(CartInfo)
PrintClients(clients)



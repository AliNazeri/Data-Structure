import collections
import csv

current_year = 2020
class Vertex:
    verteces = collections.OrderedDict()
    vertex_num=0
class person(Vertex):
    def __init__(self,arr):
        self.Job=arr[5]
        self.born_place=arr[4]
        self.born_date=arr[3]
        self.personal_code=arr[2]
        self.last_name=arr[1]
        self.name=arr[0]
    def key(self):
        return self.personal_code
    def print(self):
        print(self.name ,self.last_name ,self.personal_code ,self.born_date ,self.born_place ,self.Job)
    name="NULL"
    last_name="NULL"
    Job="NULL"
    born_place="NULL"
    born_date="NULL"
    personal_code="NULL"
class bank_account(Vertex):
    def __init__(self,arr):
        self.account_id=arr[3]
        self.IBAN_code=arr[2]
        self.bank_name=arr[1]
        self.owner_personal_code=arr[0]
    def key(self):
        return self.account_id
    owner_personal_code="NULL"
    IBAN_code="NULL"
    account_id="NULL"
    bank_name="NULL"
class home(Vertex):
    def __init__(self,arr):
        self.owner_personal_code=arr[0]
        self.cost=arr[1]
        self.post=arr[2]
        self.measurement=arr[3]
        self.address=arr[4]
    def key(self):
        return self.post
    owner_personal_code="NULL"
    cost="NULL"
    post="NULL"
    measurement="NULL"
    address="NULL"
class car(Vertex):
    def __init__(self,arr):
        self.plate=arr[0]
        self.owner_personal_code=arr[1]
        self.model=arr[2]
        self.color=arr[3]
    def key(self):
        return self.plate
    owner_personal_code="NULL"
    plate="NULL"
    model="NULL"
    color="NULL"
class phone(Vertex):
    def __init__(self,arr):
        self.oprator_name=arr[2]
        self.cim_num=arr[1]
        self.owner_personal_code=arr[0]
    def key(self):
        return self.cim_num
    owner_personal_code="NULL"
    cim_num="NULL"
    oprator_name="NULL"
class Edge:
    edges = collections.OrderedDict()
    edge_num=0
class ownership(Edge):
    def __init__(self,arr):
        self.output_cls=arr[1]
        self.input_cls=arr[0]
        self.document_code=arr[2]
        self.date_time_possession=arr[3]
        self.cost=arr[4]
    def key(self):
        return self.document_code
    input_cls="NULL"
    output_cls="NULL"
    document_code="NULL"
    date_time_possession="NULL"
    cost="NULL"
class transaction(Edge):
    def __init__(self,arr):
        self.output_cls=arr[1]
        self.input_cls=arr[0]
        self.transaction_id=arr[2]
        self.date=arr[3]
        self.amount=arr[4]
    def key(self):
        return self.transaction_id
    input_cls="NULL"
    output_cls="NULL"
    transaction_date="NULL"
    amount="NULL"
    transaction_id="NULL"
class call(Edge):
    def __init__(self,arr):
        self.duration=arr[4]
        self.call_time=arr[3]
        self.call_id=arr[2]
        self.output_cls=arr[1]
        self.input_cls=arr[0]
    def key(self):
        return self.call_id
    input_cls="NULL"
    output_cls="NULL"
    call_id="NULL"
    call_time="NULL"
    duration="NULL"
class relation(Edge):
    def __init__(self, arr):
        self.start_relation_time=arr[3]
        self.relation_type=arr[2]
        self.output_cls=arr[1]
        self.input_cls=arr[0]
        self.each_personal_code=self.input_cls+self.output_cls
    def key(self):
        return self.each_personal_code
    def _print(self):
        print(self.input_cls,self.output_cls,self.relation_type,self.start_relation_time,self.each_personal_code)
    input_cls="NULL"
    output_cls="NULL"
    relation_type="NULL"
    start_relation_time="NULL"
    each_personal_code="NULL"
class Graph_Abstract:
    vertex_edges = collections.OrderedDict()
    this_Vertex = Vertex
    this_Edge = Edge
    suspects = []
    def insertEdge(self,name,arr):
        if name=="ownership":
            tmp = ownership(arr)
        elif name=="transaction":
            tmp = transaction(arr)
        elif name=="call":
            tmp = call(arr)
        elif name=="relation":
            tmp = relation(arr)
        key = tmp.key()
        self.this_Edge.edges[key] = tmp
        self.vertex_edges[arr[0]].append(key)
        self.vertex_edges[arr[1]].append(key)
        self.this_Edge.edge_num+=1
    def insertVertices(self,name,arr):
        if name=="person":
            tmp = person(arr)
            jb = tmp.Job
            if jb=="گمرک" or jb=="سازمان بنادر":
                self.suspects.append(tmp.key())
        elif name=="bank":
            tmp = bank_account(arr)
        elif name=="home":
            tmp = home(arr)
        elif name=="phone":
            tmp = phone(arr)
        elif name=="car":
            tmp = car(arr)
        self.this_Vertex.verteces[tmp.key()] = tmp
        self.vertex_edges[tmp.key()] = []
        self.this_Vertex.vertex_num+=1
    def Faze4(self):
        this_sus = []
        Smuggler_phones = []
        for _x in self.this_Vertex.verteces:
            if isinstance(self.this_Vertex.verteces[_x],phone):
                if self.isSmugglerPhone(_x):
                    Smuggler_phones.append(_x)
        for _x in Smuggler_phones:
            for _y in self.vertex_edges[_x]:
                inp = self.this_Vertex.verteces[self.this_Edge.edges[_y].input_cls].owner_personal_code
                out = self.this_Vertex.verteces[self.this_Edge.edges[_y].output_cls].owner_personal_code
                if (inp in self.suspects):
                    if inp not in this_sus:
                        this_sus.append(inp)
                elif (out in self.suspects):
                    if out not in this_sus:
                        this_sus.append(out)
        self.update_sus(this_sus)
    def isSmugglerPhone(self,num):
        if self.this_Vertex.verteces[self.this_Vertex.verteces[num].owner_personal_code].Job == "قاچاقچی" :
            return 1
        return 0
    def Faze3(self):
        this_sus = []
        accounts =[]
        for _y in self.this_Vertex.verteces:
            _x = self.this_Vertex.verteces[_y]
            if isinstance(_x,bank_account):
                if _x.owner_personal_code in self.suspects:
                    tmp = _x.key()
                    if tmp not in accounts:
                        accounts.append(tmp)
        for _x in accounts:
            res = self.check_account_faze3(_x,7)
            #print(res)
            if res:
                if self.this_Vertex.verteces[_x].owner_personal_code not in this_sus:
                    this_sus.append(self.this_Vertex.verteces[_x].owner_personal_code)
        #print(this_sus)
        self.update_sus(this_sus)
    def isSmugglerAccount(self,BAkey):
        if self.this_Vertex.verteces[self.this_Vertex.verteces[BAkey].owner_personal_code].Job == "قاچاقچی":
            return 1
        return 0
    def check_account_faze3(self,acc,num):
        _dude = self.isSmugglerAccount(acc)
        #print(_dude)
        if _dude:
            return 1
        if num != 0:
            for _x in self.vertex_edges[acc]:
                if self.this_Edge.edges[_x].output_cls == acc:
                    res = 0
                    res = self.check_account_faze3(self.this_Edge.edges[_x].input_cls,num-1)
                    if res:
                        return 1
        else: return 0
    def Faze2(self):
        this_sus = []
        for key in self.suspects:
            _check = self.Faze2check_dude(key)
            if _check:
                if key not in this_sus:
                    this_sus.append(key)
                continue
            _x = self.vertex_edges[key]
            for y in _x:
                _z = self.this_Edge.edges[y]
                if isinstance(_z,relation):
                    if _z.output_cls==key:
                        _check = self.Faze2check_dude(_z.input_cls)
                    else: _check = self.Faze2check_dude(_z.output_cls)
                    if _check:
                        if key not in this_sus:
                            this_sus.append(key)
                        break
        self.update_sus(this_sus)
    def Faze2check_dude(self,k):
        _x = self.vertex_edges[k]
        for y in _x:
            _w = self.this_Edge.edges[y]
            if isinstance(_w,ownership):
                _z = self.Faze2check_date(2,_w)
                if _z:
                    return 1
        return 0
    def Faze2check_date(self,years,obj):
        _x = obj.date_time_possession
        _x = _x[:4]
        _x = int(_x)
        if (current_year-_x)<=2:
            return 1
        return 0
    def printing(self):
        #for x in self.suspects:
        #    self.this_Vertex.verteces[x].print()
        print(self.suspects)
    def update_sus(self,arr):
        self.suspects.clear()
        for _n in arr:
            self.suspects.append(_n)
        #for _x in self.suspects:
         #   if _x in arr:
          #      continue
           # else: self.suspects.remove(_x)

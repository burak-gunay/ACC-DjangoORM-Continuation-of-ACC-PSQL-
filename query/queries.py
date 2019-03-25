from query.models import Player, Color, Team, State

def query1(use_mpg, min_mpg, max_mpg, use_ppg, min_ppg, max_ppg,  use_rpg,  min_rpg,  max_rpg, use_apg,  min_apg, max_apg, use_spg,  min_spg, max_spg,\
            use_bpg,  min_bpg,  max_bpg):
    temp = Player.objects
    if use_mpg:
        temp = temp.filter(mpg__gte=min_mpg).filter(mpg__lte=max_mpg)
    if use_ppg:
        temp = temp.filter(ppg__gte=min_ppg).filter(ppg__lte=max_ppg)
    if use_rpg:
        temp = temp.filter(rpg__gte=min_rpg).filter(rpg__lte=max_rpg)
    if use_apg:
        temp = temp.filter(apg__gte=min_apg).filter(apg__lte=max_apg)
    if use_spg:
        temp = temp.filter(spg__gte=min_spg).filter(spg__lte=max_spg)
    if use_bpg:
        temp = temp.filter(bpg__gte=min_bpg).filter(bpg__lte=max_bpg)
    print ("PLAYER_ID TEAM_ID UNIFORM_NUM FIRST_NAME LAST_NAME MPG PPG RPG APG SPG BPG")
    for item in temp:
        print ("%d %d %d %s %s %d %d %d %d %d %d" %(item.player_id,item.team_id,item.uniform_num,item.first_name,item.last_name,item.mpg,item.ppg,item.rpg,item.apg,\
                                                   item.spg,item.bpg))
    #return [str(item.player_id)+' '+ str(item.team_id)+' '+str(item.uniform_num)+' '+item.first_name+' '+item.last_name+' '+str(item.mpg)+' '+str(item.ppg)+' '+str(item.rpg)\
    #       +' '+str(item.apg)+' '+str(item.spg)+' '+str(item.bpg) for item in temp]

def query2(team_color):
    teams = Color.objects.filter(name=team_color)
    print("NAME")
    #for item in teams:
    #    print("%s" % Team.objects.filter(color_id=item.color_id)
    retlist = list()
    return [Team.objects.filter(color_id=item.color_id) for item in teams]
    
            
def query3(team):
    print("FIRST_NAME LAST_NAME")
    tid = Team.objects.get(name=team).team_id
    return [item.first_name + ' ' + item.last_name for item in Player.objects.filter(team_id=tid).order_by('ppg')]

def query4(state,color):
    print("FIRST_NAME LAST_NAME UNIFORM_NUM")
    sid = State.objects.get(name=state).state_id #State id of given
    cid = Color.objects.get(name=color).color_id #Color id of given
    #Now, filter teams with according to sid/cid
    team = Team.objects
    teams = team.filter(state_id=sid).filter(color_id=cid)
    return [[item.first_name + ' ' + item.last_name + ' ' + str(item.uniform_num) for item in Player.objects.filter(team_id=t.team_id)] for t in teams] 

def query5(wins):
    print("FIRST_NAME LAST_NAME NAME WINS")
    teams = Team.objects.filter(wins__gte=wins)
    for team in teams:
        players = Player.objects.filter(team_id=team.team_id)
        for player in players:
            print(player.first_name + ' ' + player.last_name + ' ' + team.name + ' ' + str(team.wins)) 
    
    
#query1(1, 35, 40, 0, 3, 15, 0, 1, 7, 0, 1, 15, 0, 0.1, 0.4, 0, 0.2, 0.8)

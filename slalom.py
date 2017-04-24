from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import tools
import basic_strategy

GOLF = 0.001
SLALOM = 10.

class SlalomStrategy(Strategy):
    def __init__(self):
        super(SlalomStrategy,self).__init__("Slalom")
        
        
    def compute_strategy(self,state,id_team,id_player):
        prop =  tools.properties(state,id_team,id_player )
        bas = tools.basic_action( prop )
        zone = state.get_zones(id_team)
        
        if len(zone)==0:
                
                return basic_strategy.fonceur_base(bas)
                
        if len(zone)!=0:
            if not zone[0].dedans(state.ball.position):
                return bas.conduire(zone[0].position+Vector2D(zone[0].l,zone[0].l)/2,0.5)
            else:
                return bas.go_ball
                
           
            
            return bas.go_ball

"""team1 = SoccerTeam()
team2 = SoccerTeam()
#team1.add("John",SoloStrategy())
team1.add("John",SlalomStrategy())
simu = Parcours3(team1=team1,vitesse=SLALOM)
show_simu(simu)
simu = Parcours4(team1=team1,team2=team2,vitesse=SLALOM)
show_simu(simu)"""

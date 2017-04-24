from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import tools
import basic_strategy

GOLF = 0.001
SLALOM = 10.






class SoloStrategy(Strategy):
    def __init__(self):
        super(SoloStrategy,self).__init__("Solo")
        
        
    def compute_strategy(self,state,id_team,id_player):
        prop =  tools.properties(state,id_team,id_player )
        bas = tools.basic_action( prop )
        """ zones : liste des zones restantes a valider """
        zone = state.get_zones(id_team)
        if len(zone)==0:
            """ shooter au but """
            return basic_strategy.fonceur_base(bas)
            
            

        """ if len(zone)!=0 and prop.can_shoot:"""
        
        if len(zone)!=0:
            if prop.can_shoot and not zone[0].dedans(state.ball.position):
                return bas.passe(zone[0].position+Vector2D(zone[0].l,zone[0].l)/2)
            else:
                return bas.go_ball
            
        return bas.go_ball
        
        
"""team1 = SoccerTeam()
team2 = SoccerTeam()
team1.add("John",SoloStrategy())
team2.add("John",SoloStrategy())
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)"""
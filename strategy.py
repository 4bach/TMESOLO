# -*- coding: utf-8 -*-<

from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
import tools
import basic_strategy



GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 # Acceleration maximale de la balle

## Strategie aleatoire


class CenterStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "Random" )

    def compute_strategy( self, state, id_team, id_player ):
  
        return SoccerAction( Vector2D(), Vector2D.create_random( -0.5, 0.5 ) )
        
class FonceurStrategy( Strategy ):
    def __init__( self ):

        Strategy.__init__( self, "Fonceur" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.fonceur_base( state )

class StrikerStrategy( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "Striker" )
            
    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.striker(state )
    

class DefenceStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Defence" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.defence(state )
        
class DefenceOffStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "DefenceOff" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.defence_off(state )

    
class SoloStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Solo" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.solo(state )
    
    
class SolosupStrategy(Strategy):
    def __init__( self ):
        Strategy.__init__( self, "Solosup" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.solosup(state)
    
      
    
class StaticStrategy(Strategy):
    def __init__(self):
        super(StaticStrategy,self).__init__("Static")
    def compute_strategy(self,state,id_team,id_player):
        return SoccerAction()


#STRATEGIES 4 VS 4
class CenterStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "Random" )

    def compute_strategy( self, state, id_team, id_player ):
  
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.center(state )
    
    
class Striker4Strategy( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "Striker" )
            
    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.striker_4(state )
    

class Defence4Strategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Defence" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.defence_4(state )
    
    
    
#STRATEGIES POUR ARBRES 

class DefPlacement(Strategy):
    def __init__( self ):
        Strategy.__init__( self, "DefPlacement" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.placementdef(state)    

class Shoot( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "Shoot" )

    def compute_strategy( self, state, id_team, id_player ):

        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )

        return state.shoot_learn


class Dribble( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "Dribble" )

    def compute_strategy( self, state, id_team, id_player ):

        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        if prop.can_shoot_learn  :
            return state.shoot_learn
        return state.pousse_la_balle

class AllerBut( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "AllerBut" )

    def compute_strategy( self, state, id_team, id_player ):

        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        if prop.can_shoot_learn  :
            return state.shoot_learn
        return state.aller_but

class GoBall( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "GoBall" )

    def compute_strategy( self, state, id_team, id_player ):

        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        if prop.can_shoot_learn  :
            return state.shoot_learn
        return state.anticipe_ball( 1.5 )
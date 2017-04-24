# -*- coding: utf-8 -*-<


from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
import slalom
import golf_strategy


def get_golf_team():
    MFC = SoccerTeam( name = "MFC"  )
    
    MFC.add( "Cabra", golf_strategy.SoloStrategy( ) ) 
    return MFC
    
    
def get_slalom_team1():
    
    MFC = SoccerTeam( name = "MFC"  )
    
    MFC.add( "Cabra", slalom.SlalomStrategy( ) ) 
    return MFC
    
    
    

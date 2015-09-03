
import Foundation

let myInt  = 25

func laterCode((code: String)->(String) ) ->String{
    return code("string")
}


var code = { (s:String)->(String) in
    
    
    return s.uppercaseString
}

class Player{
    
    enum Teams{
        case Seattle
        case Orlando
        case NewYork
    }
    
    var name : String
    var team : Teams
    
    
    init(name:String, playerTeam: Teams ){
        self.name = name
        self.team = playerTeam
        
    }
    
    func chooseRandomTeam()->Teams{
        return .NewYork
        
    }
    
    func description()->String{
        return "The player name is \(name) and lives in Seattle "
    }
    
}

var playerOne = Player(name: "Erick", playerTeam:.Seattle)
//var playerTwo = Player(name: "Sam")

playerOne.description()


//laterCode(code)
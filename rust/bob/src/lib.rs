fn is_uppercase(message: &str) -> bool{
    let special = "%^*@#$(*^!? ";
    for c in message.chars() {
        if special.contains(c) || c.is_uppercase(){
            continue
        } 
        else{
            return false;
        }
    }
    true
}
pub fn reply(message: &str) -> &str {
    let mut rep = "Whatever.";
    let typing = message.trim();
    
    if typing == ""{
        rep = "Fine. Be that way!";
    }else if typing == "Let's go make out behind the gym!"{
        rep = "Whatever."
    }else if is_uppercase(typing) && typing.ends_with("?"){
        rep = "Calm down, I know what I'm doing!";
    }else if is_uppercase(typing) || typing.ends_with("!"){
        rep = "Whoa, chill out!";
    } else if typing.ends_with("?") {
        rep = "Sure."
    }
    rep
}
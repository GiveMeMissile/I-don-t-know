const NUM_LEVELS = 3;

function main() {
    let level = 1;
    let overload = 0;
    while (level <= NUM_LEVELS){
        if (level == 1){
            let completed1 = playLevel1();
            if (completed1){
                console.log("You level Up.");
                level++;
            }
        }
        if (level == 2){
            let completed2 = playLevel2();
            if (completed2){
                console.log("You level up");
                level++;
            }
        }
        if (level == 3){
            let completed3 = playLevel3();
            if (completed3){
                console.log("You level up");
                level++;
            }
        }
        overload++;
        if (overload == 15){
            level++;
            console.log("You are taking too long lol.");
        }
    }
    let replay = readBoolean("You have finished the game. Do you desire to play it again?: ");
    
    if (replay){
        main();
    }
    
}
function playLevel1(){
    let completed = false;
    let answer = readLine("You are stuck on the moon and are wearing a spacesuit. How to you get back down to earth?:");
    if (answer == "Jump to Earth"||answer == "jump to Earth"||answer == "jump to earth"||answer == "Jump to Earth"){
        completed = true;
        console.log("You jump from the moon to Earth. Congrats");
    }else if(answer == "Eat the Moon"||answer == "eat the Moon"||answer == "eat the moon"||answer == "Eat the moon"){
        console.log("You try to eat the moon. You take off your spacesuit to eat the moon and die do to a severe lack of Oxygen.");
    }else{
        console.log("An alien come out of nowhere and blasts you with a laser gun before you can act");
    }
    return completed;
}
function playLevel2(){
    let completed = false;
    let answer = readLine("You begin to fall through the atmosphere and burn up. You must save yourself?:");
    if(answer == "pray"||answer == "Pray"){
        completed = Randomizer.nextBoolean();
        if(completed){
            console.log("Your prayers have been heard and the math god saves you");
        }else{
            console.log("Your prayers are ignored and you burn up in the atmosphere");
        }
    }else if(answer == "fly"||answer=="Fly"){
        console.log("You begin to fly gracefully through the sky. Then a flying saucer flies down to you and an Alien comes out of the saucer and shoots you with a laser gun. Killing you instantly.");
    }else{
        console.log("You burn up in the atmosphere before you can act.");
    }
    return completed;

}
function playLevel3(){
    let completed = false;
    console.log("You appear in an angelic room with math equations scetched on the wall. The math god stand in front of you. The Math God after saving you requires you to answer a math question in order to be spared. If you get it incorrect the math god shall send you to the irrational plane of existance.");
    let x = Randomizer.nextInt(1,15);
    let a = Randomizer.nextInt(2,15);
    let b = Randomizer.nextInt(15, 125);
    let c = (a*x)-b;
    let answer = readInt("Solve for x, "+a+"x - "+b+" = "+c+": ");
    if (answer == x){
        completed = true;
        console.log("The math god smiles as you have answered the question correctly. The math god then sends you back to earth alive to live to tell the tail");
    }else{
        console.log("The math god grows with anger as you failed the question. The Math God then opens a portal to the irrational plane and sends you through where you shall spend the rest of your pitiful existance.");
    }
    return completed;
}
main();

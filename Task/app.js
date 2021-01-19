let cars=[]
class Car{
    constructor(_name,_model,_price){
        this.Name=_name
        this.Model=_model
        this.Price=_price
    }
    showCarDetails(){
        console.log(this.Name + "," + this.Model + "," + this.Price)
    }

}
let car01=new Car('X5','BMW',50000)
let car02=new Car('X6','BMW',70000)
let car03=new Car('Accent','Hundai',25000)
let car04=new Car('Sonata','Hundai',30000)
let car05=new Car('Samara','Lada',15000)

cars.push(car01)
cars.push(car02)
cars.push(car03)
cars.push(car04)
cars.push(car05)

function showCarByName(_carname){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Name==_carname){
            cars[i].showCarDetails()
        }
    }
}

function showCarsByPrice(_carprice){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Price>_carprice){
            cars[i].showCarDetails()
        }
    }
}

function showCarsByModel(_modelname){
    for(let i=0;i<cars.length;i++){
        if(cars[i].Model==_modelname){
            cars[i].showCarDetails()
        }
    }
}

let charCount=0;
function countChar(_word,_char){
for(let i=0;i<_word.length;i++){
    if(_word[i]==_char){
        charCount++
    }
}
console.log(charCount)
}
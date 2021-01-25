userList=[
    {
        name:'Sabir',
        email:'sabir@mail.com',
        userTasks:[
            {
                taskName:'Task01',
                taskDeadline:2
            },
            {
                taskName:'Task02',
                taskDeadline:8
            },
            {
                taskName:'Task03',
                taskDeadline:10
            }

        ]
    },
    {
        name:'Hesen',
        email:'hesen.mail.com',
        userTasks:[
            {
                taskName:'XTask01',
                taskDeadline:2
            },
            {
                taskName:'XTask02',
                taskDeadline:15
            },
            {
                taskName:'XTask03',
                taskDeadline:4
            }

        ]
    }
]
showallTasks() {
    console.log(taskName)
}
function findUserTasksByName(userName){
    // When it is entered the username show all tasks
    for (let i=0; i<userTasks.length;i++){
        if (userList[i]==userName){
            userList[i].showallTasks
        }
    }
} 
function userEmailCheck(){
    // butun istifadecilerin mail adreslerinin duzgun olub olmadigini yoxlayin (mail daxilinde @ isaretinin olub olmamasi)
    for (let i=0; i<userTasks.length;i++){
        if (email[i]===!"@"){
            return ""
        }
    }
} 
    // duzgun olmayan mail adresi varsa o mailin hansi istifadeciye aid oldugunu ekrana cap edin
function findLongestDeadline(){

    // en uzun deadlinea sahib olan taskin adini,muddetini ve o taskin hansi istifadeciye aid oldugunu ekrana cap edin
    }
    
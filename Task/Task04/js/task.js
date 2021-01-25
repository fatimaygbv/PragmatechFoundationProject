let section=document.createElement('section')
section.idName='gallery'
document.body.appendChild(section)

let container=document.createElement('div')
container.className='container'
section.appendChild(container)

for(let rowCount=0;rowCount<2;rowCount++){
    let row=document.createElement('div')
    row.className='row'
    container.appendChild(row)
    for(let colCount=0;colCount<3;colCount++){
        let col=document.createElement('div')
        col.className='col-4'
        row.appendChild(col)
    }
}
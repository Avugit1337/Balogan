function setTbl(tbl, dict) {
    let tb = tbl.getElementsByTagName('tbody')[0];
    tb.replaceChildren(tb.firstChild);
    for (key in dict)
        if (dict.hasOwnProperty(key))
            tb.appendChild(tblTr(key, dict[key]));
}

function toggleTbl(tblId, btnId, show = false) {
    const tes = document.getElementById(tblId).style;
    const ies = document.getElementById(btnId).style;
    if (show) {
        tes.removeProperty('display');
        ies.display = 'none';
    } else {
        tes.display = 'none';
        ies.removeProperty('display');
    }
}

function tblTd(txt) {
    let td = document.createElement('td');
    td.innerText = txt;
    return td;
}

function tblTr(left, right) {
    let tr = document.createElement('tr');
    tr.append(tblTd(left));
    tr.append(tblTd(right));
    return tr;
}

function toggleableTbl(container, id, toggleId, hdrLabel) {
    // Toggle btn
    const toggleProps = document.createElement('button');
    toggleProps.id = toggleId;
    toggleProps.style.marginLeft = '0px';
    toggleProps.style.marginRight = '8px';
    toggleProps.onclick = function() {toggleTbl(id, toggleId, true);};
    toggleProps.innerText = '+ ' + hdrLabel;
    container.appendChild(toggleProps);

    // Table
    const props = document.createElement('table');
    props.id = id;
    props.style.display = 'none';
    const tblBody = document.createElement('tbody');
    props.appendChild(tblBody);

    const propsTr = document.createElement('tr');
    // TblHeader
    const propsTh1 = document.createElement('th');
    propsTh1.style.float = 'left';
    propsTh1.style.width = '100%';
    propsTh1.colSpan = 2;
    propsTh1.innerText = hdrLabel;
    const propsTh1Btn = document.createElement('button');
    propsTh1Btn.onclick = function() {toggleTbl(id, toggleId);};
    propsTh1Btn.innerText = '- Hide';
    propsTh1.appendChild(propsTh1Btn);
    propsTr.appendChild(propsTh1);
    
    const propsTh2 = document.createElement('th');
    propsTh2.innerText = 'Value';

    propsTr.appendChild(propsTh2);
    tblBody.appendChild(propsTr);
    container.appendChild(props);
}

function padTwo(num) {
    return (num < 10 ? '0' : '') + num;
}

function timeFromTs(epochSeconds) {
    const d = new Date(epochSeconds * 1000);
    return padTwo(d.getHours()) + ":" + padTwo(d.getMinutes()) + ":" + padTwo(d.getSeconds());
}

function dateFromTs(epochSeconds) {
    return new Date(epochSeconds * 1000).toDateString();
}
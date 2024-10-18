const TYPE_NA = 0;
const TYPE_REGULAR = 1;
const TYPE_SUCCESS = 2;
const TYPE_BOLD = 3;
const TYPE_LINK = 4;
const TYPE_IMG = 5;
const TYPE_WARNING = 6;
const TYPE_FAILURE = 7;
const TYPE_ERROR = 8;
const TYPE_LEVEL_START = 9;
const TYPE_LEVEL_STOP = 10;
const TYPE_HTML = 11;

const TYPE_CLASSES = {
    [TYPE_NA]: 'n',
    [TYPE_REGULAR]: 'r',
    [TYPE_SUCCESS]: 's',
    [TYPE_BOLD]: 'b',
    [TYPE_LINK]: 'l',
    [TYPE_IMG]: 'i',
    [TYPE_WARNING]: 'w',
    [TYPE_FAILURE]: 'f',
    [TYPE_ERROR]: 'e',
    [TYPE_LEVEL_START]: 'L',
    [TYPE_LEVEL_STOP]: 'S',
    [TYPE_HTML]: 'h'
};

const LVL_HDR_CLASS = 'lvlHdr';
const DATA_HEIGHT_ATTR = 'data-height';
const REPORT_CONTAINER = document.getElementById('reportContainer');
const DEPTH_STEP = 15;
var lvlElements;

var lvlStack = [];
var depth = 0;

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

function setTbl(tbl, dict) {
    let tb = tbl.getElementsByTagName('tbody')[0];
    for (key in dict)
        if (dict.hasOwnProperty(key))
            tb.appendChild(tblTr(key, dict[key]));
}

function appendReportElem(element) {
    (lvlStack.length === 0 ?
        REPORT_CONTAINER
        : lvlStack[lvlStack.length - 1]).appendChild(element);
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

function timestampSpan(epoch) {
    let timestamp = document.createElement('span');
    timestamp.className = 'timeSpan';
    timestamp.innerText = timeFromTs(epoch);
    return timestamp;
}

function newReportElemDiv(elem, styleClass) {
    let elemDiv = document.createElement('div');
    elemDiv.className = styleClass;
    elemDiv.appendChild(timestampSpan(elem.e));
    return elemDiv;
}

function elemContent(data, isHtml = false) {
    let content;
    if (isHtml) {
        content = document.createElement('div');
        content.innerHTML = data;
    } else {
        content = document.createElement('span');
        content.innerText = data;
        content.className = "dataSpan";
    }
    if (depth > 0)
        content.style.marginLeft = depth + 'px';
    return content;
}

function link(elem) {
    let linkElemDiv = newReportElemDiv(elem, TYPE_CLASSES[elem.t]);
    let dataParts = elem.d.split('__', 2);
    let addressElem = document.createElement('a');
    addressElem.innerText = dataParts[1];
    addressElem.href = dataParts[0];
    if (depth > 0)
        addressElem.style.marginLeft = depth + 'px';
    linkElemDiv.appendChild(addressElem);
    appendReportElem(linkElemDiv);
}

function image(elem) {
    let imgDiv = newReportElemDiv(elem, TYPE_CLASSES[elem.t]);
    let data_parts = elem.d.split('__', 2);
    let img = document.createElement("img");
    img.src = data_parts[0];
    img.alt = data_parts[1];
    let a = document.createElement("a");
    if (depth > 0)
        a.style.marginLeft = depth + 'px';
    a.href = data_parts[0];
    a.title = data_parts[1];
    a.appendChild(img);
    imgDiv.appendChild(a);
    appendReportElem(imgDiv);
}

function regular(elem, isHtml = false) {
    let regularElemDiv = newReportElemDiv(elem, TYPE_CLASSES[elem.t]);
    regularElemDiv.appendChild(elemContent(elem.d, isHtml));
    appendReportElem(regularElemDiv);
}

function startLevel(elem) {
    let levelDiv = newReportElemDiv(elem, TYPE_CLASSES[elem.t]);
    let lvlHdrSpan = elemContent(elem.d);
    lvlHdrSpan.className = LVL_HDR_CLASS + ' H';
    levelDiv.appendChild(lvlHdrSpan);

    let lvlChildrenDiv = document.createElement('div');
    lvlChildrenDiv.className = 'Lc';
    levelDiv.appendChild(lvlChildrenDiv);

    appendReportElem(levelDiv);
    lvlStack.push(lvlChildrenDiv);
    depth += DEPTH_STEP;
}

function stopLevel() {
    if (lvlStack.length > 0) {
        lvlStack.pop();
        depth -= DEPTH_STEP;
        if (depth < 0)
            depth = 0;
    }
}

function setReportElems(reportElems) {
    let elemsMnt = reportElems.length;
    for (let i = 0; i < elemsMnt; i++) {
        switch (reportElems[i].t) {
            case TYPE_REGULAR: regular(reportElems[i]); break;
            case TYPE_SUCCESS: regular(reportElems[i]); break;
            case TYPE_BOLD: regular(reportElems[i]); break;
            case TYPE_LINK: link(reportElems[i]); break;
            case TYPE_IMG: image(reportElems[i]); break;
            case TYPE_WARNING: regular(reportElems[i]); break;
            case TYPE_FAILURE: regular(reportElems[i]); break;
            case TYPE_ERROR: regular(reportElems[i]); break;
            case TYPE_LEVEL_START: {
                let nextIdx = i + 1;
                if (nextIdx < elemsMnt && reportElems[nextIdx].t != TYPE_LEVEL_STOP) {
                    startLevel(reportElems[i]);
                } else {
                    reportElems[i].d += ' (empty)';
                    regular(reportElems[i]);
                    i = nextIdx;
                }
                break;
            }
            case TYPE_LEVEL_STOP: stopLevel(); break;
            case TYPE_HTML: regular(reportElems[i], true); break;
            default: break;
        }
    }
    lvlElements = document.getElementsByClassName(TYPE_CLASSES[TYPE_LEVEL_START]);
}

function toggleElem(el, show = false) {
    let elStyle = el.style;
    if (show) {
        elStyle.maxHeight = el.getAttribute(DATA_HEIGHT_ATTR) + 'px';
        elStyle.transform = 'scaleY(1)';
    } else {
        elStyle.maxHeight = 0;
        elStyle.removeProperty('transform');
    }
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

function toggleAllLevels(show = false) {
    for (let i = 0; i < lvlElements.length; i++) {
        let levelChildren = lvlElements[i].childNodes;
        let levelHdr = levelChildren[1];
        let isHidden = levelHdr.classList.contains('H');
        if (show) {
            if (isHidden)
                levelHdr.classList.remove('H');
        } else if (!isHidden)
            levelHdr.classList.add('H');
        toggleElem(levelChildren[2], show);
    }
}

function setLevelsOnClick() {
    for (let i = 0; i < lvlElements.length; i++) {
        let levelChildren = lvlElements[i].childNodes;
        let levelHdr = levelChildren[1];
        let levelData = levelChildren[2];
        levelHdr.onclick = function () { toggleElem(levelData, !levelHdr.classList.toggle('H')); };
        levelData.setAttribute(DATA_HEIGHT_ATTR, levelData.clientHeight);
        levelData.style.maxHeight = 0;
    }
}

function populateReport() {
    setTbl(document.getElementById('props'), report.p);
    setTbl(document.getElementById('params'), report.P);
    document.getElementById('reportHdr').innerText = "Report: " + report.n;
    document.getElementById('reportDesc').innerText = "Description: " + report.D;
    document.getElementById('started').innerText = new Date(report.S * 1000).toLocaleString();
    document.getElementById('ended').innerText = new Date(report.E[report.E.length - 1].e * 1000).toLocaleString();
    setReportElems(report.E);
    setLevelsOnClick();
}
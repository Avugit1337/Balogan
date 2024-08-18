function dce(t) { return document.createElement(t); }
function dcec(t, c) { let e = dce(t); e.className = c; return e; }
function dgei(i) { return document.getElementById(i); }
function dgec(c) { return document.getElementsByClassName(c); }
function getn(s, t) { return s.getElementsByTagName(t); }
function ac(e, c) { e.appendChild(c); }

const TYPE_REGULAR = 0;
const TYPE_SUCCESS = 1;
const TYPE_BOLD = 2;
const TYPE_LINK = 3;
const TYPE_IMG = 4;
const TYPE_WARNING = 5;
const TYPE_FAILURE = 6;
const TYPE_ERROR = 7;
const TYPE_LEVEL_START = 8;
const TYPE_LEVEL_STOP = 9;
const TYPE_HTML = 10;

const TYPE_CLASSES = {
    [TYPE_REGULAR]: 'rE',
    [TYPE_SUCCESS]: 'sE',
    [TYPE_BOLD]: 'bE',
    [TYPE_LINK]: 'lE',
    [TYPE_IMG]: 'iE',
    [TYPE_WARNING]: 'wE',
    [TYPE_FAILURE]: 'fE',
    [TYPE_ERROR]: 'EE',
    [TYPE_LEVEL_START]: 'olE',
    [TYPE_LEVEL_STOP]: 'clE',
    [TYPE_HTML]: 'hE'
};
const LVL_H_C = 'olEH';

const STATUS_INFO = 0;
const STATUS_SUCCESS = 1;
const STATUS_WARNING = 2;
const STATUS_FAILURE = 3;
const STATUS_ERROR = 4;

const STATUS_CLASSES = {
    [STATUS_INFO]: 'cW',
    [STATUS_SUCCESS]: 'cG',
    [STATUS_WARNING]: 'cY',
    [STATUS_FAILURE]: 'cO',
    [STATUS_ERROR]: 'cR'
};

const CLASSES_STATUS = {
    [STATUS_CLASSES[STATUS_INFO]]: STATUS_INFO,
    [STATUS_CLASSES[STATUS_SUCCESS]]: STATUS_SUCCESS,
    [STATUS_CLASSES[STATUS_WARNING]]: STATUS_WARNING,
    [STATUS_CLASSES[STATUS_FAILURE]]: STATUS_FAILURE,
    [STATUS_CLASSES[STATUS_ERROR]]: STATUS_ERROR
};

const REPORT_CONTAINER = dgei('rEs');
const DEPTH_STEP = 10;

var lvls = [];
var lvlsE;
var depth = 0;

function tblTd(txt) {
    let td = dce('td');
    td.innerText = txt;
    return td;
}

function tblTr(left, right) {
    let tr = dce('tr');
    ac(tr, tblTd(left));
    ac(tr, tblTd(right));
    return tr;
}

function setTbl(tbl, dict) {
    let tb = getn(tbl, 'tbody')[0];
    for (key in dict)
        if (dict.hasOwnProperty(key))
            ac(tb, tblTr(key, dict[key]));
}

function appendElement(element) {
    let sl = lvls.length;
    if (sl === 0) {
        ac(REPORT_CONTAINER, element);
    } else
        ac(lvls[sl - 1], element);
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
    let timestamp = dcec('span', 'ts');
    timestamp.innerText = timeFromTs(epoch);
    return timestamp;
}

function nRe(elem, c) {
    statusColor(elem.s);
    let div = dcec('div', c);
    ac(div, timestampSpan(elem.e));
    return div;
}

function eCont(data, h = false) {
    let content
    if (h) {
        content = dce('div');
        content.innerHTML = data;
    } else {
        content = dce('span');
        content.innerText = data;
        content.className = "ds"
    }
    if (depth > 0)
        content.style.marginLeft = depth + 'px';
    return content;
}

function statusColor(s) {
    if (s == STATUS_INFO) return;
    let sl = lvls.length;
    if (sl == 0) return;
    let c = STATUS_CLASSES[s];
    for (let i = sl - 1; i >= 0; i--) {
        let lH = lvls[i].childNodes[1];
        if (CLASSES_STATUS[lH.classList[1]] < s) {
            lH.className = LVL_H_C + ' ' + c;
        } else
            break;
    }
}

function link(elem) {
    let div = nRe(elem, TYPE_CLASSES[elem.t] + " " + STATUS_CLASSES[elem.s]);
    let d_p = elem.d.split('__', 2);
    let a = dce('a');
    a.innerText = d_p[0];
    a.href = d_p[1];
    if (depth > 0)
        a.style.marginLeft = depth + 'px';
    ac(div, a);
    appendElement(div);
}

function image(elem) {
    let div = nRe(elem, TYPE_CLASSES[elem.t] + " " + STATUS_CLASSES[elem.s]);
    let d_p = elem.d.split('__', 2);
    let i = dce("img");
    i.src = d_p[0];
    i.alt = d_p[1];
    let c = dce("a");
    if (depth > 0)
        c.style.marginLeft = depth + 'px';
    c.href = d_p[0];
    c.title = d_p[1];
    ac(c, i);
    ac(div, c);
    appendElement(div);
}

function regular(elem, h = false) {
    let div = nRe(elem, TYPE_CLASSES[elem.t] + " " + STATUS_CLASSES[elem.s]);
    ac(div, eCont(elem.d, h));
    appendElement(div);
}

function startLevel(elem) {
    let div = nRe(elem, TYPE_CLASSES[elem.t]);
    let cs = eCont(elem.d);
    cs.className = LVL_H_C + ' ' + STATUS_CLASSES[elem.s];
    ac(div, cs);
    appendElement(div);
    lvls.push(div);
    depth += DEPTH_STEP;
}

function stopLevel() {
    if (lvls.length > 0) {
        lvls.pop();
        depth -= DEPTH_STEP;
        if (depth < 0) depth = 0;
    }
}

function setRElements(rE) {
    let eMnt = rE.length;
    for (let i = 0; i < eMnt; i++) {
        console.log("Element: ");
        console.log(rE[i]);
        switch (rE[i].t) {
            case TYPE_REGULAR: regular(rE[i]); break;
            case TYPE_SUCCESS: regular(rE[i]); break;
            case TYPE_BOLD: regular(rE[i]); break;
            case TYPE_LINK: link(rE[i]); break;
            case TYPE_IMG: image(rE[i]); break;
            case TYPE_WARNING: regular(rE[i]); break;
            case TYPE_FAILURE: regular(rE[i]); break;
            case TYPE_ERROR: regular(rE[i]); break;
            case TYPE_LEVEL_START: {
                let n = i + 1;
                if (n < eMnt && rE[n].t != TYPE_LEVEL_STOP) {
                    startLevel(rE[i]);
                } else {
                    rE[i].d += ' (empty)';
                    regular(rE[i]);
                    i = n;
                }
                break;
            }
            case TYPE_LEVEL_STOP: stopLevel(); break;
            case TYPE_HTML: regular(rE[i], true); break;
            default: break;
        }
    }
    lvlsE = dgec(TYPE_CLASSES[TYPE_LEVEL_START]);
}

function getHeight(el) {
    const es = window.getComputedStyle(el);
    if (es.display !== 'none' && es.maxHeight.replace('px', '').replace('%', '') !== '0')
        return el.offsetHeight;
    return el.offsetHeight;
}

function sMh(es, mh) {
    es.maxHeight = mh;
    if (mh) {
        es.opacity = 1;
        es.removeProperty('border');
        es.removeProperty('margin');
    } else {
        es.margin = '0px';
        es.opacity = 0;
        es.border = 'none';
    }
}

function toggleSlide(el, show = false) {
    const dmh = el.getAttribute('data-max-height');
    const es = el.style;
    if (!dmh) {
        const emh = getHeight(el) + 'px';
        es.transition = 'all 0.3s ease';
        es.overflowY = 'hidden';
        es.maxHeight = 0;
        el.setAttribute('data-max-height', emh);
        es.display = el.classList.contains('olE') ? 'block' : 'flex';
        sMh(es, 0);
    } else
        sMh(es, show ? dmh : 0);
}

function toggleTbl(ti, bi, show = false) {
    const tes = dgei(ti).style;
    const ies = dgei(bi).style;
    if (show) {
        tes.removeProperty('display');
        ies.display = 'none';
    } else {
        tes.display = 'none';
        ies.removeProperty('display');
    }
}

function toggleLevel(children, show = false, toggle = false) {
    const cl = children[1].classList;
    const hidden = cl.contains('H');
    if (toggle) {
        cl.toggle('H');
    } else if (show) {
        if (hidden)
            cl.remove('H');
    } else if (!hidden)
        cl.add('H');
    for (let j = 2; j < children.length; j++) {
        toggleSlide(children[j], toggle ? hidden : show);
        if (children[j].className === TYPE_CLASSES[TYPE_LEVEL_START])
            continue;
    }
}

function toggleAllLevels(show = false) {
    for (let i = 0; i < lvlsE.length; i++)
        toggleLevel(lvlsE[i].childNodes, show);
}

function setLevelsClick() {
    for (let i = 0; i < lvlsE.length; i++)
        lvlsE[i].childNodes[1].onclick = function () { toggleLevel(lvlsE[i].childNodes, null, true); }
}

function populateReport() {
    setTbl(dgei('rp'), report.p);
    setTbl(dgei('rP'), report.P);
    dgei('rN').innerText = "Report: " + report.n;
    dgei('rD').innerText = "Description: " + report.D;
    console.log("Report:")
    console.log(report)
    setRElements(report.E);
    setLevelsClick();
    toggleAllLevels();
}
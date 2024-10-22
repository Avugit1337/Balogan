const BALOGAN_SCENARIO = 3;
const BALOGAN_REPORT = 4;

var selectedReport = null;
var lastSelectedReport = -1;
var selectedScenario = null;
var lastSelectedScenario = -1;

function registerTreeClick() {
    let toggler = document.getElementsByClassName("caret");
    for (let i = 0; i < toggler.length; i++) {
        toggler[i].addEventListener("click", function () {
            this.parentElement.querySelector(".nested").classList.toggle("active");
            this.classList.toggle("caret-down");
        });
    }
}

function genScenarioLi(propsContainer, scenario, sIdx, currUl) {
    const scenarioLi = document.createElement('li');
    currUl.appendChild(scenarioLi);

    const scenarioNameSpan = document.createElement('span');
    scenarioNameSpan.classList.add('caret');
    scenarioNameSpan.innerText = scenario.n;
    scenarioLi.appendChild(scenarioNameSpan);

    const currScenarioUl = document.createElement('ul');
    currScenarioUl.classList.add('nested');
    scenarioLi.appendChild(currScenarioUl);

    for (let i = 0; i < scenario.c.length; i++) {
        if (scenario.c[i].t === BALOGAN_REPORT) {
            const reportLi = document.createElement('li');
            reportLi.innerText = scenario.c[i].n;
            reportLi.style.cursor = 'pointer';
            reportLi.classList.add('rli');
            reportLi.onclick = function() {
                if (lastSelectedReport === i && lastSelectedScenario === sIdx)
                    return;
                lastSelectedReport = i;
                populateReport(scenario.c[i]);

                if (selectedReport != null)
                    selectedReport.classList.remove('B');
                reportLi.classList.add('B');
                selectedReport = reportLi;

                if (lastSelectedScenario === sIdx)
                    return;
                lastSelectedScenario = sIdx;
                if (selectedScenario != null)
                    selectedScenario.classList.remove('BL');
                scenarioNameSpan.classList.add('BL');
                selectedScenario = scenarioNameSpan;
                propsContainer.replaceChildren();
                toggleableTbl(propsContainer, 'scenarioProps', 'toggleScenarioProps', 'Scenario Properties');
                toggleableTbl(propsContainer, 'scenarioParams', 'toggleScenarioParams', 'Scenario Parameters');
                document.getElementById('toggleScenarioParams').style.marginRight = '0px';
                setTbl(document.getElementById('scenarioProps'), scenario.p);
                setTbl(document.getElementById('scenarioParams'), scenario.P);
            }
            currScenarioUl.appendChild(reportLi);
            reportLi.appendChild(document.createElement('br'));
        } else if (scenario.c[i].t === BALOGAN_SCENARIO)
            currScenarioUl.appendChild(genScenarioLi(propsContainer, scenario.c[i], sIdx + 1, currScenarioUl));
    }
    return scenarioLi;
}

function generateTree(scenario) {
    const treeContainer = document.createElement('div');
    treeContainer.id = 'treeContainer';
    const treeHdr = document.createElement('h3');
    treeHdr.innerText = 'Scenario Tree';
    treeHdr.style.marginBottom = '0px';
    treeContainer.appendChild(treeHdr);
    const scenarioTree = document.createElement('ul');
    scenarioTree.id = 'scenarioTree';
    const scenarioPContainer = document.createElement('div');
    scenarioTree.appendChild(genScenarioLi(scenarioPContainer, scenario, 0, scenarioTree));
    treeContainer.appendChild(scenarioTree);
    treeContainer.appendChild(scenarioPContainer);
    return treeContainer;
}

function populateScenario(scenario) {
    const scenarioBody = document.getElementById('scenarioBody');
    scenarioBody.replaceChildren();
    scenarioBody.appendChild(generateTree(scenario));
    const reportBody = document.createElement('div');
    reportBody.id = 'reportBody';
    scenarioBody.appendChild(reportBody);
    registerTreeClick();
}
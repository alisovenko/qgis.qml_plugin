import QtQuick 1.0

FocusScope {
    id: focusScope
    width: 250; height: 28

    BorderImage {
        source: "images/lineedit-bg.png"
        width: parent.width; height: parent.height
        border { left: 4; top: 4; right: 4; bottom: 4 }
    }

    BorderImage {
        source: "images/lineedit-bg-focus.png"
        width: parent.width; height: parent.height
        border { left: 4; top: 4; right: 4; bottom: 4 }
        visible: parent.activeFocus ? true : false
    }

    Text {
        id: typeSomething
        anchors.fill: parent; anchors.leftMargin: 8
        verticalAlignment: Text.AlignVCenter
        text: "Double click to choose file ..."
        color: "black"
        font.italic: false
    }

    MouseArea { 
        anchors.fill: parent
        onClicked: { 
            //console.log("FocusScope Clicked");
            focusScope.focus = true;
        }
        onDoubleClicked: { 
            console.log("Chose file Clicked");
            focusScope.focus = true;
            
            typeSomething.text = mainwindow.selectFile;
        }
    }

}

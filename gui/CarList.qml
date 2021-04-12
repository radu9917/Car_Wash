import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    id:root
    width:400
    height:1000

    Button {
        id: button
        x: 8
        y: 8
        text: qsTr("add car")
    }

    Button {
        id: button1
        x: 150
        y: 8
        text: qsTr("delete car")
    }

    Button {
        id: button2
        x: 292
        y: 8
        text: qsTr("update car")
    }

    ListView {
        id: listView
        anchors.fill: parent
        anchors.topMargin: 83
        model: model
        delegate: CarDelegate{}
    }
}

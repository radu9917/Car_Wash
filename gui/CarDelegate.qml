import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Templates 2.12 as T

T.Button {
    id:root
    property string owner:ownerLabel.text
    property string number:numberLabel.text
    width:400
    height:70
    autoExclusive: true
    onCheckedChanged: {
        if(checked)
            rectangle.color ="#ffffff"
        else
            rectangle.color = "#e5e5e5"
    }


    Rectangle {
        id: rectangle
        color: "#e5e5e5"
        anchors.fill: parent

        Label {
            id: ownerLabel
            text: "owner"
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            font.pointSize: 15
            anchors.leftMargin: 20
        }

        Label {
            id: numberLabel
            text: "Number"
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            font.pointSize: 15
            anchors.rightMargin: 20
        }
    }
}

# Basic-GUI-desktop-app-using-PyQt5

This app consist of two input textbox and one file upload.
The textbox is made by QLineEdit() method and the label for that field is made by QLabel() method.
```
For label:-
self.nameLabel_1 = QLabel(self)
self.nameLabel_1.setText('Name:')

For Textfield:-
self.textbox_1 = QLineEdit(self)
```

The width and height is set by move() method and resize() method was used to fit the prefect width and height of the textfield.
### For example:-
```
self.textbox_1.move(95, 20)  act as move(x-coordinate, y-coordinate)
self.textbox_1.resize(260,30)  act as resize(x-coordinate, y-coordinate)
```

setStyleSheet() method is used to gave styling to all the field's and buttons. That is font, color..etc.
The syntax for styling inside setStyleSheet() method is similar to normal CSS that is use for Web-development. 

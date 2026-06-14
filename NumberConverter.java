import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.ScrollPane;
import javafx.scene.control.TextArea;
import javafx.event.ActionEvent;
import javafx.geometry.Pos;
import javafx.geometry.HPos;
import javafx.collections.ObservableList;
import javafx.collections.FXCollections;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.File;
import javafx.scene.control.Alert;
import java.lang.ProcessBuilder;
import java.util.Scanner;

public class NumberConverter extends Application{

    private TextField inputField;
    private TextField outputField;
    private Label inputLabel;
    private Label outputLabel;
    private Button convertButton;
    private Button infoButton;
    private Button clear;
    private Button swapButton;
    private CheckBox signedButton;
    private Label inputMenuLabel;
    private ComboBox<String> inputModeMenu;
    private Label outputMenuLabel;
    private ComboBox<String> outputModeMenu;
    private ObservableList<String> forms;

    public void start(Stage primaryStage){
        primaryStage.setTitle("Number Converter App");
        primaryStage.setResizable(false);

        inputField = new TextField();
        inputField.setPrefWidth(150);
        outputField = new TextField();
        outputField.setPrefWidth(150);

        inputLabel = new Label("Input:");
        outputLabel = new Label("Output:");

        convertButton = new Button("Convert");
        convertButton.setOnAction(this::convert);

        clear = new Button("Clear Both Fields");
        clear.setOnAction(this::clearFields);

        signedButton = new CheckBox("Signed");
        signedButton.setIndeterminate(false);

        infoButton = new Button("ⓘ");
        infoButton.setOnAction(this::showInfo);

        swapButton = new Button("Swap");
        swapButton.setOnAction(this::swap);

        inputMenuLabel = new Label("From:");
        outputMenuLabel = new Label("To:");

        forms = FXCollections.observableArrayList(
            "Binary",
            "Decimal",
            "Hexadecimal",
            "Roman"
        );
        inputModeMenu = new ComboBox<>(forms);
        inputModeMenu.setOnAction(this::outputMenuModifier);
        outputModeMenu = new ComboBox<>();
        outputModeMenu.setOnAction(this::signedButtonSwitch);
        setDefaultOptions();


        GridPane menuPane = new GridPane();
        menuPane.setAlignment(Pos.CENTER);
        menuPane.setHgap(20);
        menuPane.setVgap(15);
        menuPane.add(inputMenuLabel, 0, 0);
        menuPane.add(inputModeMenu, 1, 0);
        menuPane.add(signedButton, 2, 0);
        menuPane.add(outputMenuLabel, 0, 1);
        menuPane.add(outputModeMenu, 1, 1);
        menuPane.add(swapButton, 2, 1);

        GridPane ioPane = new GridPane();
        ioPane.setAlignment(Pos.CENTER);
        ioPane.setHgap(20);
        ioPane.setVgap(15);
        ioPane.add(inputLabel, 0, 0);
        ioPane.add(inputField, 1, 0, 2, 1);
        ioPane.add(outputLabel, 0, 1);
        ioPane.add(outputField, 1, 1, 2, 1);

        GridPane buttonPane = new GridPane();
        buttonPane.setAlignment(Pos.CENTER);
        buttonPane.setHgap(20);
        buttonPane.add(clear, 0, 0);
        buttonPane.add(infoButton, 1, 0);
        buttonPane.add(convertButton, 2, 0);

        GridPane mainPane = new GridPane();
        mainPane.setAlignment(Pos.CENTER);
        mainPane.setVgap(25);
        mainPane.add(menuPane, 0, 0);
        mainPane.add(ioPane, 0, 1);
        mainPane.add(buttonPane, 0, 2);

        Scene myScene = new Scene(mainPane, 370, 280);

        primaryStage.setScene(myScene);
        primaryStage.show();

    }


    public void clearFields(ActionEvent event){
        inputField.clear();
        outputField.clear();
    }

    public void convert(ActionEvent event){
        String input = inputField.getText().trim();

        if (input.length() == 0){
            showError("Input cannot be empty.");
            return;
        }

        try{
            convertHelp(input);
        }
        catch(IOException ioe){
            showError("Problem with input.");
        }
        catch(InterruptedException ie){
            showError("Interrupted flow.");
        }

    }

    private void convertHelp(String input) throws IOException, InterruptedException{

        String mode = "" + signedButton.isSelected();
        String inputMode = inputModeMenu.getValue();
        String outputMode = outputModeMenu.getValue();

        if(inputMode == null || outputMode == null){
            showError("You must choose your modes first.");
            return;
        }

        ProcessBuilder pb = new ProcessBuilder("python", "backend_script.py", inputMode, outputMode, input, mode);
        Process process = pb.start();

        String output = new String (process.getInputStream().readAllBytes());
        output = output.trim();

        String error = new String (process.getErrorStream().readAllBytes());
        error = error.trim();

        int successCode = process.waitFor();

        if (successCode == 0){
            outputField.setText(output);
        }

        else{
            showError(error);
        }
    }

    private void showError(String message){

        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Error");
        alert.setHeaderText("An Error Occured");
        alert.setContentText(message);
        alert.showAndWait();

    }

    public void showInfo(ActionEvent event){
        Stage infoPopup = new Stage();
        infoPopup.setTitle("Help Info");
        infoPopup.setResizable(false);
        String infoText = readHelpFile("Help.txt");
        if(infoText == null){
            return;
        }
        TextArea infoArea = new TextArea(infoText);
        infoArea.setWrapText(true);
        infoArea.setEditable(false);
        infoArea.setStyle("-fx-font-family: monospace;");
        infoArea.setPrefSize(600, 300);
        GridPane infoPane = new GridPane();

        infoPane.add(infoArea, 0, 0);

        Scene infoScene = new Scene(infoPane, 600, 300);

        infoPopup.setScene(infoScene);
        infoPopup.show();

    }

    private String readHelpFile(String fileName){

        File file = new File(fileName);
        Scanner fileScanner = null;
        String result = "";

        try{
            fileScanner = new Scanner(file);
            fileScanner.useDelimiter("//Z");

            if(fileScanner.hasNext()){
                result = fileScanner.next();
            }

        }

        catch (FileNotFoundException fnfe){
            showError("Help file not found. Make sure you have downloaded the " +
                      "help.txt file and placed it in the right folder.");
            return null;
        }

        finally{
            if (fileScanner != null){
                fileScanner.close();
            }
        }

        return result;

    }

    public void outputMenuModifier(ActionEvent event){
        outputMenuModifierHelp();
    }

    private void outputMenuModifierHelp(){

        String curr = inputModeMenu.getValue();
        ObservableList<String> outputMenuList = FXCollections.observableArrayList();

        for(int i = 0; i < forms.size(); i++){
            outputMenuList.add(forms.get(i));
        }

        outputMenuList.removeAll(curr);
        outputModeMenu.setItems(outputMenuList);
        outputModeMenu.setValue(null);

    }

    private void setDefaultOptions(){
        inputModeMenu.setValue("Decimal");
        outputMenuModifierHelp();
        outputModeMenu.setValue("Binary");
    }

    private void signedButtonSwitch(ActionEvent event){
        
        String inputValue = inputModeMenu.getValue();
        String outputValue = outputModeMenu.getValue();

        if(outputValue == null){
            return;
        }

        if((inputValue.equals("Decimal") && !outputValue.equals("Roman")) || 
            (outputValue.equals("Decimal") && !inputValue.equals("Roman"))){
            signedButton.setDisable(false);
        }

        else{
            signedButton.setDisable(true);
        }

    }

    public void swap(ActionEvent event){

        String newInputMenuValue = outputModeMenu.getValue();
        String newOutputMenuValue = inputModeMenu.getValue();

        inputModeMenu.setValue(newInputMenuValue);
        outputMenuModifierHelp();
        outputModeMenu.setValue(newOutputMenuValue);

    }

}
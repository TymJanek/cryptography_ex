package com.company;

public class Caesar {

    private String text;
    private int shift;

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public int getShift() {
        return shift;
    }

    public void setShift(int shift) {
        this.shift = shift;
    }

    public Caesar(String text, int shift) {
        this.text = text;
        this.shift = shift;
    }

    public StringBuilder cipher(){
        StringBuilder result = new StringBuilder();

        for(char character : text.toCharArray()){
            int originalAlphabetPosition = character - 'a';
            if(originalAlphabetPosition >= 0 && originalAlphabetPosition <= 26){
                int newAlphabetPosition = (originalAlphabetPosition + this.shift) % 26;
                char newCharacter = (char) ('a' + newAlphabetPosition);

                result.append(newCharacter);
            }
            else{
                result.append(character);
            }

        }


        return result;
    }

    public String toString(){
        return ("Original message: " + text);
    }
}

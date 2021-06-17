package com.company;

import java.awt.*;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;
import java.util.Random;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int shift;

        System.out.println("Type message You want to be ciphered with usage of Caesar Cipher: ");
        Scanner sc1 = new Scanner(System.in);
        String message = sc1.nextLine();

        System.out.println("Your message may be ciphered using either random or selected by your value. \n 1). Random \n 2). Selected ");
        Scanner sc2 = new Scanner(System.in);
        System.out.print("Please pick your method: (1,2) ");
        int choice = sc2.nextInt();

        if(choice == 1){
            Random rand = new Random();
            shift = rand.nextInt(26);
        }
        else{
            System.out.print("Please select value of which the letters in message will be shifted: ");
            Scanner sc3 = new Scanner(System.in);
            shift = sc3.nextInt();
        }

        Caesar c1 = new Caesar(message, shift);
        System.out.println(c1);
        System.out.println("Message has been shifted by " + shift);
        System.out.println("Shifted message: " + c1.cipher());

        //choice whether to copy ciphered message into clipboard
        System.out.print("Do you want the message to be copied into your clipboard? (Y/N) ");
        Scanner sc4 = new Scanner(System.in);
        String clipboardChoice = sc4.nextLine().toUpperCase();
        if(clipboardChoice.equals("Y") || clipboardChoice.equals("YES")){
            StringSelection selection = new StringSelection(c1.cipher().toString());
            Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
            clipboard.setContents(selection, selection);
            System.out.println("Ciphered message has been copied successfully into Your clipboard.");
        }

    }
}

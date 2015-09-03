

import mx.unam.ciencias.edd.*;
import java.util.*;
import java.math.*;
import java.io.*;

/**
 * Zona de ensayos
 */

public class ZonaJava {

    public static void main(String[] args) {
        
        String m  = "";
        
        File f = new File("../Shared/outFile.txt");
        if(!f.exists())
            return ;
        
//        String delimitadores= "[ .,;?!¡¿\'\"\\[\\]]+";
        
        Lista<String> elementos = new Lista<String>();
        Lista<Integer> valores = new Lista<Integer>();
        try
        {
            BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream(f)));
            String line;
            while ((line = in.readLine()) != null) {

                String[] parts = line.split("\t");
                elementos.agregaFinal(parts[0]); // 004
                valores.agregaFinal(Integer.valueOf(parts[1]));
            }
            in.close();
        }
        catch(IOException ioe)
        {
            System.out.printf("El archivo tiene un error, o no existe.\n");
        }
        
        
        Histograma<String> bigHistograma =  new Histograma<String>("Fibonacci");
        
        bigHistograma.agrega(elementos,valores);
        
        System.out.println(bigHistograma.toScalableVectorGraphicsBars(true,0,true,true,false));
        
//        Histograma<String> h = new Histograma<String>("Fibonacci");
//        h.agrega(elementos, valores);
        
//        Lista<String> l = new Lista<String>();
//        l.agregaFinal("Hola");
//        l.agregaInicio("Hey");
////        System.out.println(l);
//        Diccionario<String,Integer> d = new Diccionario<String,Integer>();
//        
//        d.agrega("one",1);
//        d.agrega("two",2);
//        d.agrega("three",3);
//        
////        System.out.println(d);
//        
//        BigInteger big = new BigInteger("234567");
//        String file = open("../Shared/outFile.txt");
//        
//        List<String> lista = new ArrayList<String>();
//        lista.add("12");
        
//       print(file , new File("../Shared/outFile.txt"));
//        System.out.println(new BigInteger(file));
       
    }
    private static void print(String stringToWrite, File file)
    {
        
        try {
            FileOutputStream fileOut = new FileOutputStream(file);
            OutputStreamWriter osOut = new OutputStreamWriter(fileOut);
            BufferedWriter out = new BufferedWriter(osOut);
            out.write(stringToWrite);
            out.close();
            
        } catch (IOException ioe) {
            System.exit(1);
        }
    }
    
    public static String open(String nombreArchivo)
    {
        String m  = "";
        
        File f = new File(nombreArchivo);
        if(!f.exists())
            return null;
        
        String delimitadores= "[ .,;?!¡¿\'\"\\[\\]]+";
        try
        {
            BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream(f)));
            String line;
            while ((line = in.readLine()) != null) {
                
                m+=line;
            }
            in.close();
        }
        catch(IOException ioe)
        {
            System.out.printf("El archivo %s tiene un error, o no existe.\n",nombreArchivo);
        }
        
        
        return m;
    }
}

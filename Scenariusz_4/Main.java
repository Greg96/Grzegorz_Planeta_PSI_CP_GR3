import java.util.Random;

/**
 * Created by Grzegorz Płaneta on 18.01.2018.
 */
public class Main {
    public static void main(String[] args)
    {
        double learningRate=0.9;

        double forgetRate=learningRate/5;//wspolczynnik zapominania

        int numbOfLetters=20;
        int epochs=10;
        int sizeOfLetter=35;

        Data data=new Data();
        double[][] trainingData=new double[numbOfLetters][sizeOfLetter];
        for(int i=0;i<20;i++)
        {
            trainingData[i]=data.getData(i);
        }

        double[] weights=generateW(sizeOfLetter);
        //Zaczynam nauke
        System.out.println("Przed treningiem: ");
        printW(weights,sizeOfLetter);
        weights=train(weights,trainingData,learningRate,forgetRate,epochs,numbOfLetters);
        System.out.println("PO: ");
        printW(weights,sizeOfLetter);
        //testowanie
        System.out.println("Testujemy: ");
        for(int i=0;i<20;i++)
        {
            System.out.println("Wartość net dla liczby "+i+" wynosi: "+activate(weights,data.getData(i),35));
        }
    }
    private static void printW(double[] W,int size)
    {
        System.out.println("Wagi wynosza: ");
        for(int i=0;i<size;i++)
        {
            System.out.println(W[i]+"/n");
        }
    }
    private static double[] generateW(int n)
    {
        Random rand=new Random();
        double[] weights=new double[n];
        for(int i=0;i<n;i++)
        {
            weights[i]=rand.nextInt(10)+1;
            weights[i]=weights[i]/10;
        }
        return weights;
    }
    private static double[] updateW(double net,double[] W,double[] data, double learningRate,double forgetRate, int size)
    {
        double newW[]=new double[size];
        for(int i=0;i<size;i++)
        {
            newW[i]=(1-forgetRate)*W[i]+learningRate*Math.signum(net)*data[i];
        }
        return newW;
    }
    private static double activate(double[] W,double[] data, int size)
    {
        double net=0;
        for(int i=0;i<size;i++)
        {
            net+=W[i]*data[i];
        }
        return net;
    }
    private static double[] train(double[] W,double[][] data, double learningRate, double forgetRate, int epochs, int numbOfLetters)
    {
        double net;
        for(int i=0;i<epochs;i++)
        {
            for(int j=0;j<numbOfLetters;j++)
            {
                net=activate(W,data[j],35);
                W=updateW(net,W,data[j],learningRate,forgetRate,35);
            }
        }
        for(int j=0;j<100;j++)//aktywujemy wybrana litere by moc ja rozpoznac
        {
            net=activate(W,data[10],35);
            W=updateW(net,W,data[10],learningRate,forgetRate,35);
        }
        return W;
    }

}

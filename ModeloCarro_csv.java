import weka.core.converters.CSVLoader;
import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
import weka.classifiers.trees.J48;
import weka.classifiers.trees.RandomForest;
import java.io.File;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
public class ModeloCarro_csv {
 public static void main(String[] args) throws Exception {


 // dataset de treinamento (2/3) e dataset de teste (1/3)


 // Para Carregar um arquivo CSV
 CSVLoader loader = new CSVLoader();
 loader.setSource (new File("car5.csv"));
 Instances train = loader.getDataSet();
 if (train.classIndex() == -1)
 train.setClassIndex(train.numAttributes() - 1);

 // Para Carregar um arquivo CSV
 CSVLoader loader2 = new CSVLoader();
 loader2.setSource (new File("tempo.nominal_teste.csv"));
 Instances test = loader2.getDataSet();
 if (test.classIndex() == -1)
 test.setClassIndex(test.numAttributes() - 1);

 // train classifier
 Classifier cls = new J48();
 cls.buildClassifier(train);
 System.out.println(cls.toString() );
 // evaluate classifier and print some statistics
 Evaluation eval = new Evaluation(train);
 eval.evaluateModel(cls, test);
 System.out.println(eval.toSummaryString("\nResultado:\n======\n", false));
 System.out.println(eval.toMatrixString() );


 // train classifier
 Classifier cls2 = new RandomForest();
 cls2.buildClassifier(train);
 System.out.println(cls2.toString() );

 // evaluate classifier and print some statistics
 Evaluation eval2 = new Evaluation(train);
 eval2.evaluateModel(cls2, test);
 System.out.println(eval2.toSummaryString("\nResultado:\n======\n", false));
 System.out.println(eval2.toMatrixString() );


 }
}
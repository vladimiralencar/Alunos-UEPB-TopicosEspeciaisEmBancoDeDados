import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Attribute;
import weka.core.DenseInstance;
import weka.core.Instances;
import weka.core.Instance;
import weka.classifiers.lazy.IBk;
import weka.classifiers.trees.J48;
public class ModeloPredicao {
 public static void main(String[] args) throws Exception {
 //------------------------------------------------------
 // (1) importação da base de dados de treinamento
 //------------------------------------------------------
 DataSource source = new DataSource("tempo.nominal.arff");
 Instances D = source.getDataSet();

 // 1.1 - espeficicação do atributo classe
 if (D.classIndex() == -1) {
 D.setClassIndex(D.numAttributes() - 1);
 }
 //------------------------------------------------------
 // (2) Construção do modelo classificador (treinamento)
 //------------------------------------------------------

 J48 j48 = new J48();

 j48.buildClassifier(D);

 //------------------------------------------------------
 // (3) Classificando um novo exemplo
 //------------------------------------------------------

 // 3.1 criação de uma nova instância

 Instance newInst = new DenseInstance(4);
 newInst.setDataset(D);
 newInst.setValue(0, "ensolarado");
 newInst.setValue(1, "quente");
 newInst.setValue(2, "normal");
 //newInst.setValue(3, "forte");
 newInst.setValue(3, "fraco");
 // 3.2 classificação de uma nova instância
 double pred = j48.classifyInstance(newInst);
 // 3.3 imprime o valor de pred
 System.out.println("Predição: " + pred);

 // 3.4 imprime a string correspondente ao valor de pred
 Attribute a = D.attribute(4);
 String predClass = a.value((int) pred);
 System.out.println("Predição: " + predClass);

 }
}
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

struct Resistor {
    int node1, node2;
    double resistance;
};

class Circuit {
public:
    vector<Resistor> resistors;

    void addResistor(int node1, int node2, double resistance) {
        resistors.push_back({node1, node2, resistance});
    }

    double calculateEquivalentResistance() {
        while (resistors.size() > 1) {
            for (int i = 0; i < resistors.size(); i++) {
                int node1 = resistors[i].node1;
                int node2 = resistors[i].node2;
                double R1 = resistors[i].resistance;

                // Check for series or parallel connection
                for (int j = 0; j < resistors.size(); j++) {
                    if (i != j && isSeries(node1, node2, resistors[j])) {
                        double R2 = resistors[j].resistance;
                        double R_eq = R1 + R2;
                        mergeNodes(i, j, R_eq);
                        break;
                    }
                    else if (i != j && isParallel(node1, node2, resistors[j])) {
                        double R2 = resistors[j].resistance;
                        double R_eq = 1 / (1/R1 + 1/R2);
                        mergeNodes(i, j, R_eq);
                        break;
                    }
                }
            }
        }
        return resistors[0].resistance;
    }

private:
    bool isSeries(int node1, int node2, Resistor r) {
        // Checks for series connection
        return (node1 == r.node1 && node2 == r.node2);
    }

    bool isParallel(int node1, int node2, Resistor r) {
        // Checks for parallel connection
        return (node1 == r.node1 || node2 == r.node2);
    }

    void mergeNodes(int i, int j, double R_eq) {
        // Merges two resistors into one
        resistors[i].resistance = R_eq;
        resistors.erase(resistors.begin() + j);
    }
};

int main() {
    Circuit circuit;
    circuit.addResistor(1, 2, 5);
    circuit.addResistor(2, 3, 10);
    circuit.addResistor(3, 4, 15);
    circuit.addResistor(4, 5, 20);

    double result = circuit.calculateEquivalentResistance();
    cout << "Equivalent Resistance: " << result << " Ohms" << endl;

    return 0;
}

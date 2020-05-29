# HTML Privacy Policy to Plaintext Converter

This repository hosts the source code for converting HTML representations of privacy policies to plaintext. Note that the purpose of preprocessing is to allow for deeper NLP processing (e.g., POS tagging, dependency parsing, NER). Therefore, the process includes a heuristic to form complete sentences from formatted lists, which may result in duplicated text in the output and may not preserve word count frequencies. The current implementation uses the langdetect Python module to ignore non-English policies. Full details of the approach can be found in Appendix A of the PolicyLint paper listed below. 


# Instructions:

* Place HTML privacy policies in ./ext/html\_policies

* Build the docker image: $ ./build.sh

* Run the docker image: $ ./run.sh

* The output will be in ./ext/plaintext\_policies


# Publication

Full details of the approach can be found in Appendix A of the PolicyLint paper listed below:

Benjamin Andow, Samin Yaseer Mahmud, Wenyu Wang, Justin Whitaker, William Enck, Bradley Reaves, Kapil Singh, and Tao Xie. PolicyLint: Investigating Internal Privacy Policy Contradictions on Google Play, Proceedings of the USENIX Security Symposium (SECURITY), August 2019. Santa Clara, CA, USA.


# License

The HTML Privacy Policy to Plaintext Converter is licensed under the GPL v3.0 License (See LICENSE.txt).

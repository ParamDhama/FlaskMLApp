$(document).ready(function() {
    $('#prediction-form').submit(function(event) {
        event.preventDefault();
        var selectedModel = $('#model-select').val();
        $.ajax({
            url: '/predict',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                model: selectedModel,
                features: [
                    parseFloat($('#sepal-length').val()),
                    parseFloat($('#sepal-width').val()),
                    parseFloat($('#petal-length').val()),
                    parseFloat($('#petal-width').val())
                ]
            }),
            success: function(response) {
                var name;
                if (response.prediction == 0) {
                    name = "Iris setosa"
                }
                else if (response.prediction == 1) {
                    name = "Iris versicolor"
                }
                else if (response.prediction == 2) {
                    name = "Iris virginica"
                }
                else {
                    name = "can't identify"
                }
                var predictionResult = 'Predicted Class: ' + name;
                $('#prediction-result').text(predictionResult);
            }
        });
    });
});

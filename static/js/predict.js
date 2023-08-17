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
                var predictionResult = 'Predicted Class: ' + response.prediction;
                $('#prediction-result').text(predictionResult);
            }
        });
    });
});

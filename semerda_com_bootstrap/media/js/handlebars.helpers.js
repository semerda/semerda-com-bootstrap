var helpers = function() {

    var name_index = 0;

    // General
    Handlebars.registerHelper('index_set', function() {
        name_index++;
        return name_index;
    });
    Handlebars.registerHelper('index_get', function() {
        return name_index;
    });
    Handlebars.registerHelper('index_reset', function() {
        name_index = 0;
    });

    // Twitter bootstrap
    Handlebars.registerHelper('btn', function(btn_type, text) {
      text = Handlebars.Utils.escapeExpression(text);
      var result = '<a href="#" class="btn ' + btn_type + '">' + text + '</a>';
      return new Handlebars.SafeString(result);
    });

}();
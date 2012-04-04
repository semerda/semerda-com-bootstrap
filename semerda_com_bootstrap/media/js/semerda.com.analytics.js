/*
 * Google Analytic (GA) methods
 * v0.1
 * By Ernest Semerda
 * Semerda.com
 *
 */

SEMERDA.analytics = (function () {

    return {
      // Track specific outgoing URL
      // Usage: onclick="ga_out(this, 'Outbound Links', 'blog-trtsv');return false;"
      qa_out: function(link, category, action) {
        _gat._getTrackerByName()._trackEvent(category, action);
        setTimeout('document.location = "' + link.href + '"', 100);
      },

      // Bind all specific links using regex, no code required in html markup
      ga_bind: function(regex, category, action) {
        $(regex == '' ? 'a[href]' : 'a[href$="'+regex+'"]').click(function() {
          // Default is most common, a click
          action = action || "click";
          // Get label name from data-ga else from the text attribute
          var label = (this.hasAttribute('data-ga') ? 
                          this.attributes.getNamedItem('data-ga').value : 
                          $(this).text());
          // Google analytics push - http://code.google.com/apis/analytics/docs/tracking/eventTrackerGuide.html
          _gaq.push(['_trackEvent', category, action, label, $(this).attr('href')]);
        });
      }
      
    }

}());
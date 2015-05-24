var app = angular.module('TrackApp', [
    'TimeTrackControllers',
    'ngRoute',
]);

function get_static(path) {
    return '/static/' + path;
}

app.config(function($routeProvider, $locationProvider) {
    $routeProvider.when("/", {
        controller: "TimeTrackCtrl",
        templateUrl: get_static("/partials/time_track.html")
  });
});

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl("/api");
    RestangularProvider.setRequestSuffix("/");
});

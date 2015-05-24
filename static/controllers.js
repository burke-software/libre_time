var appp = angular.module('TimeTrackControllers', ['restangular', 'angucomplete-alt']);


appp.controller('TimeTrackCtrl',
        ['$scope', 'Restangular' , function (
            $scope, Restangular) {
    Restangular.all('tasks').getList()
    .then(function(tasks) {
        $scope.tasks = tasks;
    })
}]);

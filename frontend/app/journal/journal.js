'use strict';

angular.module('myApp.journal', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/journal', {
            templateUrl: 'journal/journal.html',
            controller: 'journalCtrl'
        });
    }])


    .controller('journalCtrl', ["Restangular", "$scope", function (Restangular, $scope) {
        Restangular.all('journal-entries').getList().then(function (journalEntries) {
            $scope.journalEntries = journalEntries;


        })
    }]);